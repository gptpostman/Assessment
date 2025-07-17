from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from ..services.class_service import get_classes_service
from ..schemas.schemas import ClassResponse
from ..database import get_db
from typing import List
from datetime import datetime

router = APIRouter()

@router.get("/", response_model=List[ClassResponse])
def get_classes(
    db: Session = Depends(get_db),
    tz: str = Query("Asia/Kolkata", description="Timezone, e.g., 'Asia/Kolkata', 'UTC', 'America/New_York'"),
    instructor: str = Query(None),
    date_from: datetime = Query(None),
    date_to: datetime = Query(None)
):
    return get_classes_service(db, tz, instructor, date_from, date_to)