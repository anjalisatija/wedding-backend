from fastapi import FastAPI
from app.routes.booking import router as booking_router

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Backend is working"}

app.include_router(booking_router)
