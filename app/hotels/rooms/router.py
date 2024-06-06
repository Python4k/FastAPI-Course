from app.hotels.router import router as hotels_router


@hotels_router.get("/{hotel_id}/rooms")
async def get_rooms(hotel_id: int):
    pass