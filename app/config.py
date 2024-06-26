from pydantic_settings import BaseSettings
from pydantic import model_validator

class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    JWT_SECRET_KEY: str
    ALGHORITHM: str
    
    class Config:
        env_file = '.env'

settings = Settings()

DATABASE_URL = f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASS}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
