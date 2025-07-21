from .base import BaseModel
from sqlalchemy.orm import mapped_column, relationship, Mapped
from sqlalchemy import Numeric, Date, ForeignKey
import datetime

class WeatherData(BaseModel):
    __tablename__ = "weather_data"

    date: Mapped[datetime.date] = mapped_column(Date)
    temp_min: Mapped[float] = mapped_column(Numeric(3, 1))
    temp_max: Mapped[float] = mapped_column(Numeric(3, 1))
    temp_mean: Mapped[float] = mapped_column(Numeric(3, 1))
    precip_sum: Mapped[float] = mapped_column(Numeric(5, 2))
    rain_sum: Mapped[float] = mapped_column(Numeric(5, 2))
    snow_sum: Mapped[float] = mapped_column(Numeric(5, 2))
    sunsh_time: Mapped[int] = mapped_column()
    wind_dir: Mapped[int] = mapped_column()
    weather_code: Mapped[int] = mapped_column()
    location_id: Mapped[int] = mapped_column(ForeignKey("location.id"))

    location: Mapped["Location"] = relationship(back_populates="weather_data")
