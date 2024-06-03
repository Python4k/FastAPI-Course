import jwt
import app.exceptions as exceptions

from jwt.exceptions import PyJWTError
from datetime import datetime, timedelta, UTC
from passlib.context import CryptContext
from pydantic import EmailStr
from fastapi import Depends, HTTPException, Request, status

from app.config import settings
from app.users.controller import UserController



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data: dict, expires_delta: int = None):
    to_encode = data.copy()
    expire = datetime.now(UTC) + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.ALGHORITHM)
    return encoded_jwt
    

async def authenticate_user(email: EmailStr, password: str):
    user = await UserController.get_one_or_none(email=email)
    if user and verify_password(password, user.password): 
        return user
    return None

def get_token(request: Request):
    token = request.cookies.get("access_token")
    if not token:
        raise exceptions.EXPIREDACCESS
    return token

async def get_current_user(token: str = Depends(get_token)):

    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, settings.ALGHORITHM)
    except PyJWTError:
        raise exceptions.TOKENINVALID
    expire: str = payload.get("exp")
    if (not expire) or (int(expire) < datetime.now(UTC).timestamp()):
        raise exceptions.EXPIREDACCESS
    user_id: str = payload.get("sub")
    if user_id is None:
        raise exceptions.INCORRECTDATA
    user = await UserController.get_by_id(id=int(user_id))
    if user is None:
        raise exceptions.INCORRECTDATA
    return user