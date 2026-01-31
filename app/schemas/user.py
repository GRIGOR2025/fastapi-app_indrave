from pydantic import BaseModel
from enum import Enum

class UserRole(str, Enum):
    PASSENGER = "passenger"
    DRIVER = "driver"

class User(BaseModel):
    id: int
    username: str
    role: UserRole
    rating: float = 5.0