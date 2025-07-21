from .base import BaseModel
from sqlalchemy.orm import mapped_column, relationship, Mapped
from sqlalchemy import String, Numeric

class Location(BaseModel):
    __tablename__ = "location"

    city: Mapped[str] = mapped_column(String(64))
    country: Mapped[str] = mapped_column(String(64))
    latitude: Mapped[float] = mapped_column(Numeric(12, 9))
    longitude: Mapped[float] = mapped_column(Numeric(12, 9))
    is_active: Mapped[bool] = mapped_column(default=True)

    weather_data: Mapped[list["WeatherData"]] = relationship(back_populates="location")