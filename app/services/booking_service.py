from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..models.models import FitnessClass, Booking
# from ..schemas.schemas import BookingRequest, BookingConfirmationResponse, BookingDetails, BookingResponseAll, BookingRescheduleRequest, BookingRescheduleResponse, BookingDeleteResponse
from ..schemas.schemas import *
from ..utils.convert_time import convert_utc_to_ist

# def get_class_by_id(db: Session, class_id: int):
#     return db.query(FitnessClass).filter(FitnessClass.id == class_id).first()

def book_class_service(request: BookingRequest, db: Session):
    cls = db.query(FitnessClass).filter(FitnessClass.id == request.class_id).first()
    # cls = get_class_by_id(db, request.class_id)
    if not cls:
        raise HTTPException(status_code=404, detail="class not found")

    existing = db.query(Booking).filter(
        Booking.class_id == request.class_id,
        Booking.client_email == request.client_email
    ).first()

    if existing:
        return BookingConfirmationResponse(
            message = "You already booked this class.",
            details = BookingDetails(
                booking_id = existing.id,
                class_name = cls.name,
                client_email = existing.client_email
            )
        )

    if cls.available_slots <= 0:
        raise HTTPException(status_code=400, detail="no slots available")

    booking = Booking(
        class_id=request.class_id,
        client_name=request.client_name,
        client_email=request.client_email
    )
    cls.available_slots -= 1
    db.add(booking)
    db.commit()
    db.refresh(booking)
    return BookingConfirmationResponse(
        message=f"Booking confirmed for {request.client_name}",
        details=BookingDetails(
            booking_id=booking.id,
            class_name=cls.name,
            client_email=booking.client_email
        )
    )

def get_bookings_service(mail: str, db: Session):
    return db.query(Booking).filter(Booking.client_email == mail).all()

def get_all_bookings_service(db: Session):
    bookings = db.query(Booking).all()
    result = []

    for booking in bookings:
        class_obj = db.query(FitnessClass).filter(FitnessClass.id == booking.class_id).first()
        result.append(
            BookingResponseAll(
                booking_id = booking.id,
                class_id = booking.class_id,
                class_name = class_obj.name if class_obj else "",
                client_name = booking.client_name,
                client_email = booking.client_email,
                datetime = convert_utc_to_ist(class_obj.datetime) if class_obj else None
            )
        )
    return result

def reschedule_booking_service(booking_id:int, req: BookingRescheduleRequest, db: Session):
    booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")

    old_class = db.query(FitnessClass).filter(FitnessClass.id == booking.class_id).first()
    new_class = db.query(FitnessClass).filter(FitnessClass.id == req.new_class_id).first()
    if not new_class:
        raise HTTPException(status_code=404, detail="New class not found")
    if new_class.available_slots <= 0:
        raise HTTPException(status_code=400, detail="No slots available in new class")

    # Update slots
    if old_class:
        old_class.available_slots += 1
    new_class.available_slots -= 1

    # Update booking
    booking.class_id = req.new_class_id
    db.commit()
    db.refresh(booking)
    return BookingRescheduleResponse(
        message = "Booking rescheduled successfully",
        booking_id = booking.id,
        old_class_id = old_class.id if old_class else None,
        new_class_id = new_class.id,
        client_name = booking.client_name,
        client_email = booking.client_email
    )

def delete_booking_service(booking_id:int, db:Session):
    booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    fitness_class = db.query(FitnessClass).filter(FitnessClass.id == booking.class_id).first()
    if fitness_class:
        fitness_class.available_slots += 1

    response = BookingDeleteResponse(
        booking_id = booking.id,
        class_name = fitness_class.name if fitness_class else "",
        client_name = booking.client_name,
        client_email = booking.client_email
    )

    db.delete(booking)
    db.commit()
    return response