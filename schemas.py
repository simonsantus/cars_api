from pydantic import BaseModel

class Car(BaseModel):
    id: int
    brand: str
    model: str
    year: int
    fuel_type: str
    power: int
    max_speed: int