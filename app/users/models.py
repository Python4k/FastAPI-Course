from app.database.models import Base
from sqlalchemy import JSON, Column, Computed, ForeignKey, Integer, String, Date
from datetime import date

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
