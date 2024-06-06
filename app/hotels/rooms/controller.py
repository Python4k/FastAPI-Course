from sqlalchemy import select

from app.database.controller import BaseController
from app.hotels.rooms.models import Room
from app.database.controller import async_session


class RoomController(BaseController):
    model = Room

