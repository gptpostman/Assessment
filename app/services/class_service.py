from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..models.models import FitnessClass
from ..schemas.schemas import ClassResponse
import pytz
from ..utils.convert_time import convert_utc_to_ist

def get_classes_service(db: Session, tz: str, instructor: str, date_from, date_to):
    try:
        user_tz = pytz.timezone(tz)
    except pytz.UnknownTimeZoneError:
        raise HTTPException(status_code=400, detail="Invalid timezone")

    query = db.query(FitnessClass)
    if instructor:
        query = query.filter(FitnessClass.instructor.ilike(f"%{instructor}%"))
    if date_from:
        query = query.filter(FitnessClass.datetime >= date_from.astimezone(pytz.UTC))
    if date_to:
        query = query.filter(FitnessClass.datetime <= date_to.astimezone(pytz.UTC))

    classes = query.all()
    return [
        ClassResponse(
            id=cls.id,
            name=cls.name,
            datetime=convert_utc_to_ist(cls.datetime),
            instructor=cls.instructor,
            available_slots=cls.available_slots
        ) for cls in classes
    ]