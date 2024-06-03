from fastapi import APIRouter, HTTPException, Response
from app.users.auth import authenticate_user, create_access_token, get_password_hash
from app.users.controller import UserController
from app.users.schemas import SchemaUserAuth

router = APIRouter(
    prefix="/auth",
    tags=["Auth and Users"],
)

@router.post("/register")
async def register_user(user_data: SchemaUserAuth):
    existing_user = await UserController.get_one_or_none(email=user_data.email)
    if existing_user:
        return HTTPException(status_code=400, detail="User with this email already exists")
    hashed_password = get_password_hash(user_data.password)
    await UserController.add(email=user_data.email, password=hashed_password)
    
    
@router.post("/login")
async def login_user(response: Response, user_data: SchemaUserAuth):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        return HTTPException(status_code=401, detail="Incorrect email or password")
    access_token = create_access_token(data={"sub": user.id})
    response.set_cookie(key="access_token", value=f"Bearer {access_token}", httponly=True)
    return access_token
    
        