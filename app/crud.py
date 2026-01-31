from sqlalchemy.orm import Session
from app.models import Offer
from app.schemas.offer import OfferCreate

def create_offer(db: Session, offer_data: OfferCreate):
    db_offer = Offer(
        ride_id=offer_data.ride_id,
        proposed_price=offer_data.proposed_price,
        driver_name="Driver_Ivan" # Временно
    )
    db.add(db_offer)
    db.commit()
    db.refresh(db_offer)
    return db_offer

def get_offers_for_ride(db: Session, ride_id: int):
    return db.query(Offer).filter(Offer.ride_id == ride_id).all()