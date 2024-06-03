from datetime import date
from fastapi import APIRouter, Depends, Request

from app import exceptions
from app.bookings.controller import BookingController
from app.bookings.schemas import SchemaBooking
from app.users.auth import get_current_user
from app.users.models import User


router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"],
)

@router.get("/")
async def get_all_bookings(user: User = Depends(get_current_user)):
    return await BookingController.get_all_by_filter(user_id=user.id)

@router.post("/")
async def add_booking(room_id: int, date_from: date, date_to: date, user: User = Depends(get_current_user)):
    booking = await BookingController.add(user_id=user.id, room_id=room_id, date_from=date_from, date_to=date_to)
    if not booking:
        raise exceptions.ROOMCANNOTBEBOOKED