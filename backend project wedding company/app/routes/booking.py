from fastapi import APIRouter
from pydantic import BaseModel
from app.database import db

router = APIRouter()

class Booking(BaseModel):
    name: str
    event_type: str
    date: str
    guests: int

@router.post("/book")
async def create_booking(booking: Booking):
    result = await db.bookings.insert_one(booking.dict())
    return {
        "message": "Booking created successfully",
        "id": str(result.inserted_id)
    }

@router.get("/bookings")
async def get_bookings():
    bookings = []
    async for booking in db.bookings.find():
        booking["_id"] = str(booking["_id"])
        bookings.append(booking)
    return bookings
