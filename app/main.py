import sys
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import uvicorn.lifespan

from app.bookings.router import router as bookings_router
from app.users.router import router as users_router

app = FastAPI(version="0.3.0")

app.include_router(users_router)
app.include_router(bookings_router)

@app.get("/")
async def root():
    return RedirectResponse("/docs")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=8000, reload=True)
    