# Wedding Booking Backend (FastAPI)

This is a backend service built using **FastAPI** for managing wedding bookings.

## Features
- Create a wedding booking
- Fetch all bookings
- MongoDB integration
- Interactive API docs using Swagger

## Tech Stack
- Python
- FastAPI
- MongoDB
- Uvicorn

## API Endpoints
- `GET /` → Health check
- `POST /book` → Create a booking
- `GET /bookings` → Get all bookings

## How to Run
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
