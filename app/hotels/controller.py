from sqlalchemy import select

from app.database.controller import BaseController
from app.hotels.models import Hotel
from app.database.controller import async_session


class HotelController(BaseController):
    model = Hotel
