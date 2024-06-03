from app.database.controller import BaseController
from app.users.models import User

class UserController(BaseController):
    model = User