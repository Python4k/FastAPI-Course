from datetime import datetime, timedelta, UTC
from passlib.context import CryptContext
from pydantic import EmailStr
from app.config import settings
import jwt
from app.users.controller import UserController

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: int = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(UTC) + expires_delta
    else:
        expire = datetime.now(UTC) + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.ALGHORITHM)
    return encoded_jwt

async def authenticate_user(email: EmailStr, password: str):
    user = await UserController.get_one_or_none(email=email)
    if user and verify_password(password, user.password): 
        return user
    return None
