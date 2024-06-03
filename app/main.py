from fastapi import FastAPI

from app.bookings.router import router as bookings_router
from app.users.router import router as users_router

app = FastAPI(version="0.2.0")

app.include_router(users_router)
app.include_router(bookings_router)

@app.get("/")
def root():
    return 'root page'
