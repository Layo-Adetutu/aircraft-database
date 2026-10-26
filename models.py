from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Aircraft(Base):
    __tablename__ = "aircrafts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    reg_number = Column(String)
    price = Column(Float)
    country = Column(String)
    speed = Column(Integer)








