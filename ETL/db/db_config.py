from dotenv import load_dotenv
import os
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()
db_url = os.getenv("DATABASE_URL")

logger = logging.getLogger(__name__)

try:
    Base = declarative_base()
    engine = create_engine(db_url)
    Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
except Exception as error:
    logger.error(f"Unexpected error happenned: {error}")

def get_db():
    db_session = Session()
    try:
        yield db_session
    finally:
        db_session.close()