from fastapi import APIRouter



router = APIRouter(
    prefix="/hotels",
    tags=["Hotels"],
)

@router.get("/")
async def get_hotels():
    pass