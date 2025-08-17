from sqlalchemy.orm import Session
from sqlalchemy import func
from db.models import WeatherData, Location
import datetime
import requests
import time
import logging

logger = logging.getLogger(__name__)

SLEEP_TIME = 240
TOO_MANY_REQUESTS_STATUS_CODE = 429
MIN_START_DATE = datetime.date(1950, 1, 1)
DEFAULT_DATE_TO = datetime.date.today() - datetime.timedelta(days=5)
DELTA_STEP = datetime.timedelta(days=7500)
DELTA_ONE_DAY = datetime.timedelta(days=1)
URL = "https://archive-api.open-meteo.com/v1/archive?latitude={lat}&longitude={lon}&start_date={start_date}&end_date={end_date}" \
"&daily=weather_code,temperature_2m_max,temperature_2m_min,temperature_2m_mean,rain_sum,precipitation_sum,sunshine_duration,snowfall_sum,wind_direction_10m_dominant"


def get_date_from(db: Session, location_id: int) -> str:
    last_date = db.query(func.max(WeatherData.date)).filter(WeatherData.location_id == location_id).scalar()
    last_date = last_date + DELTA_ONE_DAY if last_date != DEFAULT_DATE_TO and last_date else last_date
    return last_date if last_date else MIN_START_DATE

def build_date_to(date_from: datetime.date, date_to: datetime.date) -> datetime.date:
    time_delta = date_to - date_from
    return date_from + DELTA_STEP if time_delta > DELTA_STEP - DELTA_ONE_DAY else date_to

def weather_data_service(db: Session, location: Location, date_to=DEFAULT_DATE_TO):
    date_from = get_date_from(db=db, location_id=location.id)

    if date_from > date_to:
        raise Exception(f"Bad date parameters: {date_from} & {date_to}!")
    
    while date_from < date_to:
        date_to_step = build_date_to(date_from=date_from, date_to=date_to)
        daily_data = extract_weather_data(lat=location.latitude, lon=location.longitude, date_from=date_from, date_to=date_to_step)
        parsed_daily_data = parse_weather_data(daily_data=daily_data, location_id=location.id)
        insert_weather_data(db=db, weather_data=parsed_daily_data)

        date_from = date_from + DELTA_STEP + DELTA_ONE_DAY

def extract_weather_data(lat: float, lon: float, date_from: str, date_to: str):
    url = URL.format(lat=lat, lon=lon, start_date=date_from, end_date=date_to)
    response = requests.get(url)
    iteration_ind = 1
    try:
        while True:
            if response.status_code == requests.codes.ok:
                break
            if response.status_code == TOO_MANY_REQUESTS_STATUS_CODE:
                now = datetime.datetime.now()
                iteration_sleep_time = SLEEP_TIME * iteration_ind
                delta = datetime.timedelta(seconds=iteration_sleep_time)
                print(f"Went to sleep..be back at {now + delta}")
                time.sleep(iteration_sleep_time)
                response = requests.get(url)
                iteration_ind = iteration_ind + 1
            else: 
                response.raise_for_status()
        return response.json().get("daily")
    except Exception as error:
        logger.error(f"Unexpected error happenned: {error}. Response data: {response.status_code}, {response.text}")

def parse_weather_data(daily_data: str, location_id: int) -> list[WeatherData]:
    time = daily_data.get("time")
    weather_code = daily_data.get("weather_code")
    temp_max = daily_data.get("temperature_2m_max")
    temp_min = daily_data.get("temperature_2m_min")
    temp_mean = daily_data.get("temperature_2m_mean")
    rain_sum = daily_data.get("rain_sum")
    precip_sum = daily_data.get("precipitation_sum")
    sunshine_dur = daily_data.get("sunshine_duration")
    snow_sum = daily_data.get("snowfall_sum")
    wind_dir = daily_data.get("wind_direction_10m_dominant")

    if not len(time):
        raise Exception(f"Bad json structure: {daily_data}")
    
    weather_data: list[WeatherData] = []
    for idx, date in enumerate(time):
        wd_instance = WeatherData(date=date, temp_min=temp_min[idx], temp_max=temp_max[idx], temp_mean=temp_mean[idx],
                                  precip_sum=precip_sum[idx], rain_sum=rain_sum[idx], snow_sum=snow_sum[idx], wind_dir=wind_dir[idx],
                                  sunsh_time=int(sunshine_dur[idx]/60), weather_code=weather_code[idx], location_id=location_id)
        weather_data.append(wd_instance)
    return weather_data

def insert_weather_data(db: Session, weather_data: list[WeatherData]):
    db.add_all(weather_data)
    db.commit()