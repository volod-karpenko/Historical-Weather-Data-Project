from sqlalchemy.orm import Session
from db.models import Location

def get_locations(db: Session, is_active: bool) -> list[Location]:
    query = db.query(Location)
    if is_active != None:
        query = query.filter(Location.is_active == is_active)
    return query.all()
