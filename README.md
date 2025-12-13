## Wedding Booking Backend (FastAPI)

This project is a backend application developed using FastAPI for managing wedding event bookings.
It provides REST APIs to create and retrieve booking data and uses MongoDB for persistent storage.

The backend follows a clean and modular FastAPI structure with separate files for application startup,
database configuration, and API routes.

## What the Project Does
- Accepts wedding booking details through REST APIs
- Stores booking data in MongoDB
- Retrieves all stored bookings from the database
- Provides Swagger UI for testing APIs

## Tech Stack
- Python
- FastAPI
- MongoDB (Atlas)
- Uvicorn
- Motor (Async MongoDB driver)

## API Endpoints

## GET /
Used to check whether the backend is running.

## POST /book
Creates a new wedding booking and stores it in MongoDB.

## Sample Request Body:
```json
{
  "name": "Anjali",
  "event_type": "Wedding",
  "date": "2025-02-10",
  "guests": 200
}
```

## GET /bookings
Fetches all wedding bookings stored in the MongoDB database.

## Swagger UI is enabled in this project and is available locally at:
[http://127.0.0.1:8001/docs](http://127.0.0.1:8000/docs)
Note: The port may vary if changed while running uvicorn.

## How to Run the Project

Create and activate a virtual environment

python -m venv .venv
.venv\Scripts\activate


## Install required dependencies

pip install fastapi uvicorn motor python-dotenv


Run the FastAPI server

uvicorn app.main:app --reload --port 8001


Open Swagger UI in the browser

http://127.0.0.1:8001/docs

## Database

MongoDB Atlas is used as the database

Booking data is stored in the bookings collection

MongoDB connection is handled asynchronously using Motor

## Notes

This is a backend-only project

No frontend is included

Environment variables are managed using .env

Project follows FastAPI best practices

