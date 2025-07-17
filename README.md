# Fitness App Backend

A modular backend API for managing fitness classes and bookings, built with FastAPI, SQLAlchemy, and Pydantic.

---

## Features

- **Fitness Classes:** List, filter by instructor, date, and timezone.
- **Bookings:** Create, view, reschedule, and delete bookings.
- **Time Conversion:** Automatic conversion between UTC and IST.
- **Modular Architecture:** Clean separation of controllers, services, models, schemas, and utilities.

---

## Project Structure

```
app/
├── main.py
├── base.py
├── database.py
├── controllers/
│   ├── class_controller.py
│   └── booking_controller.py
├── services/
│   ├── class_service.py
│   └── booking_service.py
├── models/
│   └── models.py
├── schemas/
│   └── schemas.py
└── utils/
    └── convert_time.py
```

---

## Setup & Installation

1. **Clone the repository:**
   ```
   git clone <your-repo-url>
   cd fitness_app_new/app
   ```

2. **Install dependencies:**
   ```
   pip install fastapi sqlalchemy pydantic uvicorn pytz
   ```

3. **Run the server:**
   ```
   uvicorn main:app --reload
   ```

4. **Access the API docs:**
   - Open [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your browser.

---

## API Endpoints

### Classes

- `GET /classes/`  
  List all classes, filter by instructor, date, and timezone.

### Bookings

- `POST /bookings/`  
  Create a new booking.
- `GET /bookings/?mail=<client_email>`  
  Get bookings for a specific client.
- `GET /bookings/all`  
  Get all bookings.
- `PUT /bookings/{booking_id}/reschedule`  
  Reschedule a booking to a different class.
- `DELETE /bookings/{booking_id}`  
  Delete a booking.

---

## Libraries Used

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [pytz](https://pypi.org/project/pytz/)
- [Uvicorn](https://www.uvicorn.org/) (ASGI server)

---

## Notes

- Database is SQLite and will be created automatically on first run.
- Initial class data is seeded at startup.
- All time conversions use the utility in `utils/convert_time.py`.

---

## License

MIT License

---
