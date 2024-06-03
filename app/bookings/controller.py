from app.database.controller import BaseController
from app.bookings.models import Booking

class BookingController(BaseController):
    model = Booking