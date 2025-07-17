from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .base import Base
from .models.models import FitnessClass, Booking
from datetime import datetime, timedelta

SQLALCHEMY_DATABASE_URL = "sqlite:///./fitness.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

def create_db_and_tables():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def seed_data():
    from sqlalchemy.orm import Session
    db = SessionLocal()
    if not db.query(FitnessClass).first():
        now = datetime.utcnow()
        classes = [
            FitnessClass(
                name="Yoga",
                datetime=now + timedelta(days=1),
                instructor="Alice",
                total_slots=10,
                available_slots=10
            ),
            FitnessClass(
                name="Zumba",
                datetime=now + timedelta(days=2),
                instructor="Bob",
                total_slots=8,
                available_slots=8
            ),
            FitnessClass(
                name="HIIT",
                datetime=now + timedelta(days=3),
                instructor="Charlie",
                total_slots=12,
                available_slots=12
            )
        ]
        db.add_all(classes)
        db.commit()
    db.close()