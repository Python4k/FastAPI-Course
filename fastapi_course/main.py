from datetime import date
from typing import Optional
from fastapi import FastAPI, Query
from pydantic import BaseModel

hotels = [
    {
        "address": "221B Baker Street",
        "name": "The Ritz-Carlton, London",
        "stars": 5
    },
    {
        "address": "123 London Road",
        "name": "Grand Hyatt London",
        "stars": 4
    },
    {
        "address": "123B Baker Street",
        "name": "Hilton London",
        "stars": 3
    },
    {
        "address": "12 London Road",
        "name": "Holiday Inn London",
        "stars": 4
    }
]

class SHotel(BaseModel):
    address: str
    name: str
    stars: int
    

class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date

app = FastAPI()


@app.get("/")
def root():
    return 'root page'


@app.get("/hotels")
def get_hotels(location: str,
               date_from: date,
               date_to: date,
               stars: Optional[int] = Query(None, ge=1, le=5),
               has_spa: Optional[bool] = None
) -> list[SHotel]:
    return hotels


@app.post("/bookings")
def add_booking(booking: SBooking):
    pass