from pydantic import BaseModel

class OfferCreate(BaseModel):
    ride_id: int
    proposed_price: float

class OfferResponse(OfferCreate):
    id: int
    driver_name: str
    status: str

    class Config:
        from_attributes = True