from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
# from ..services.booking_service import book_class_service, get_bookings_service, get_all_bookings_service, delete_booking_service, reschedule_booking_service
from ..services.booking_service import *
# from ..schemas.schemas import BookingRequest, BookingConfirmationResponse, BookingResponse, BookingResponseAll, BookingRescheduleRequest, BookingRescheduleResponse, BookingDeleteResponse
from ..schemas.schemas import *
from ..database import get_db
from typing import List

router = APIRouter()

@router.post("/", response_model=BookingConfirmationResponse)
def book_class(request: BookingRequest, db: Session = Depends(get_db)):
    return book_class_service(request, db)

@router.get("/", response_model=List[BookingResponse])
def get_bookings(mail: str = Query(...), db: Session = Depends(get_db)):
    return get_bookings_service(mail, db)

@router.get("/all", response_model=list[BookingResponseAll])
def get_all_bookings(db: Session = Depends(get_db)):
    return get_all_bookings_service(db)

@router.put("/{booking_id}/reschedule", response_model = BookingRescheduleResponse)
def reschedule_booking(booking_id: int, req: BookingRescheduleRequest, db: Session = Depends(get_db)):
    return reschedule_booking_service(booking_id, req, db)

@router.delete("/{booking_id}",response_model=BookingDeleteResponse)
def delete_booking(booking_id:int, db: Session = Depends(get_db)):
    return delete_booking_service(booking_id, db)


