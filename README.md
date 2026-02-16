# Cloud-Based Wedding Booking Management API

A production-ready backend API built using FastAPI for managing wedding event bookings.  
This system allows users to create and retrieve booking records via RESTful endpoints.  
The application is deployed on cloud infrastructure and connected to MongoDB Atlas.

---

##  Live Deployment

Base URL:
https://wedding-backend-pt26.onrender.com

Interactive API Documentation (Swagger UI):
https://wedding-backend-pt26.onrender.com/docs

---

## Tech Stack

- Python
- FastAPI
- MongoDB Atlas (Cloud Database)
- Motor (Async MongoDB Driver)
- Uvicorn
- Render (Cloud Deployment)
- RESTful API Architecture

---

##  Features

- Create new wedding bookings
- Retrieve all stored bookings
- Cloud database integration (MongoDB Atlas)
- Fully deployed backend on Render
- Interactive Swagger UI for API testing
- Modular and clean project structure

---

##  API Endpoints

### GET /
Health check endpoint to verify backend status.

### POST /book
Creates a new wedding booking.

Sample Request:
{
  "name": "Anjali",
  "event_type": "Wedding",
  "date": "2025-02-10",
  "guests": 200
}

### GET /bookings
Fetches all stored wedding bookings.

---

##  Project Structure

- main.py – Application entry point
- database.py – MongoDB configuration
- routes/ – API route definitions

---

This project demonstrates backend development, cloud deployment, REST API design, and database integration skills.
