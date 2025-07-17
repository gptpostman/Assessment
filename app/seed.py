from .models.models import FitnessClass
from datetime import datetime, timedelta

def seed_data(db):
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