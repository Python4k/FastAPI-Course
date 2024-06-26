from app.database.models import Base
from sqlalchemy import JSON, Column, Integer, String, ForeignKey
from datetime import date

class Hotel(Base):
    __tablename__ = "hotels"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    services = Column(JSON)
    rooms_quantity = Column(Integer , nullable=False)
    image_id = Column(Integer)
    
    