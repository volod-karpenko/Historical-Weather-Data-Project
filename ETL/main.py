from logger.logger_setup import setup_logging
setup_logging(log_level="INFO")

import logging 
from db.db_config import get_db
from db.methods.location import get_locations
from db.methods.weather_data import weather_data_service

logger = logging.getLogger(__name__)

try:
    for db in get_db():
        locations = get_locations(db=db, is_active=True)
        for location in locations:
            weather_data_service(db=db, location=location)
except Exception as error:
    logger.error(f"Unexpected error happenned: {error}")
