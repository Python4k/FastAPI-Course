from fastapi import APIRouter

from app.bookings.controller import BookingController
from app.bookings.schemas import SchemaBooking




router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"],
)

@router.get("/")
async def get_all_bookings() -> list[SchemaBooking]:
    return await BookingController.get_all()
