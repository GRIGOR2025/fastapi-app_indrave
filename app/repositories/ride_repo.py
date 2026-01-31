from sqlalchemy.orm import Session
from app.models import RideModel

class RideRepository:
    def create_ride(self, db: Session, ride_data: dict):
        db_ride = RideModel(**ride_data)
        db.add(db_ride)
        db.commit()
        db.refresh(db_ride)
        return db_ride

    def get_by_id(self, db: Session, ride_id: int):
        return db.query(RideModel).filter(RideModel.id == ride_id).first()


    def get_active(self, db: Session):
        return db.query(RideModel).filter(RideModel.status == "searching").all()


    def update_status(self, db: Session, ride_id: int, driver_id: int, new_status: str):
        db_ride = self.get_by_id(db, ride_id)
        if db_ride:
            db_ride.status = new_status
            db_ride.driver_id = driver_id
            db.commit()
            db.refresh(db_ride)
        return db_ride