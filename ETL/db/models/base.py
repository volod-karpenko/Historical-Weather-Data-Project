from db.db_config import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import DateTime
from sqlalchemy.sql import func
import datetime

class BaseModel(Base):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
