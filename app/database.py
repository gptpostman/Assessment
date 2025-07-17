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
        