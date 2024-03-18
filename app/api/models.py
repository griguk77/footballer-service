from pydantic import BaseModel
from typing import List, Optional


class FootballerIn(BaseModel):
    name: str
    country: str
    goals: int
    age: int
    clubs_id: int


class FootballerOut(FootballerIn):
    id: int


class FootballerUpdate(FootballerIn):
    name: Optional[str] = None
    country: Optional[str] = None
    goals: Optional[int] = None
    age: Optional[int] = None
    clubs_id: Optional[int] = None
