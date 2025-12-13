from fastapi import APIRouter
from app.database import db

router = APIRouter()

@router.post("/book")
async def create_booking(data: dict):
    result = await db.bookings.insert_one(data)
    return {
        "message": "Booking created",
        "id": str(result.inserted_id)
    }
