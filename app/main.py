from fastapi import FastAPI
from .controllers.class_controller import router as class_router
from .controllers.booking_controller import router as booking_router
from .database import create_db_and_tables, seed_data

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    seed_data()

app.include_router(class_router, prefix="/classes", tags=["Classes"])
app.include_router(booking_router, prefix="/bookings", tags=["Bookings"])