from pydantic import BaseModel

class AircraftCreate(BaseModel):
    name: str
    reg_number: str
    price: float
    country: str
    speed: int