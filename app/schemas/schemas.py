from pydantic import BaseModel
from datetime import datetime

class ClassResponse(BaseModel):
    id: int
    name: str
    datetime: datetime
    instructor: str
    available_slots: int

    class Config:
        orm_mode = True

class BookingRequest(BaseModel):
    class_id: int
    client_name: str
    client_email: str

class BookingDetails(BaseModel):
    booking_id: int
    class_name: str
    client_email: str

class BookingConfirmationResponse(BaseModel):
    message: str
    details: BookingDetails

class BookingResponse(BaseModel):
    id: int
    class_id: int
    client_name: str
    client_email: str

class BookingDeleteResponse(BaseModel):
    booking_id: int
    class_name: str
    client_name: str
    client_email: str

class BookingResponseAll(BaseModel):
    booking_id: int
    class_id: int
    class_name: str
    client_name: str
    client_email: str
    datetime: datetime

class BookingRescheduleRequest(BaseModel):
    new_class_id: int

class BookingRescheduleResponse(BaseModel):
    booking_id: int
    old_class_id: int | None=None
    new_class_id: int
    client_name: str
    client_email: str
    message: str

    class Config:
        orm_mode = True