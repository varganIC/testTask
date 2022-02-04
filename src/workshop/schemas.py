from typing import List, Optional
from pydantic import BaseModel
from datetime import date


class Car(BaseModel):
    id: int
    driver: str
    number: str
    year_release: date
    color: str
    speed: int
    description: Optional[str] = None
    owner_id: int

    class Config:
        orm_mode = True


class CarModel(BaseModel):
    id: int
    brand: str
    child: List[Car] = []

    class Config:
        orm_mode = True
