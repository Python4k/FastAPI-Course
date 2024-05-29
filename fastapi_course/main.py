from datetime import date
from typing import Optional
from fastapi import FastAPI, Query
from pydantic import BaseModel


class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date

app = FastAPI()


@app.get("/")
def root():
    return 'root page'


@app.get("/hotels")
def get_hotels(location: str, date_from: date, date_to: date, stars: Optional[int] = Query(None, ge=1, le=5), has_spa: Optional[bool] = None):
    return { "location": location, "date_from": date_from, "date_to": date_to, "stars": stars, "has_spa": has_spa }


@app.post("/bookings")
def add_booking(booking: SBooking):
    pass