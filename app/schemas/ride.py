from pydantic import BaseModel

# Это то, что мы ждем от пользователя
class RideCreate(BaseModel):
    start_point: str
    end_point: str
    price: int
