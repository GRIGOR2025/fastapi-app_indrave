from sqlalchemy.orm import Session
from app.repositories.ride_repo import RideRepository
from app.schemas.ride import RideCreate


class RideService:
    def __init__(self):
        self.ride_repo = RideRepository()

    def create_new_ride(self, db: Session, ride_info: RideCreate, passenger_id: int):
        # Превращаем Pydantic-схему в словарь
        ride_data = ride_info.model_dump()

        # Если в Swagger поле "pickup_location", а в БД "start_point", переименуй ключ:
        if "pickup_location" in ride_data:
            ride_data["start_point"] = ride_data.pop("pickup_location")
        if "destination" in ride_data:
            ride_data["end_point"] = ride_data.pop("destination")

        ride_data["passenger_id"] = passenger_id
        ride_data["status"] = "searching"

        return self.ride_repo.create_ride(db, ride_data)

    def get_active_orders(self, db: Session):
        # Вызываем метод, который мы только что создали в репозитории
        return self.ride_repo.get_active(db)

    def accept_ride(self, db: Session, ride_id: int, driver_id: int):
        ride = self.ride_repo.get_by_id(db, ride_id)
        if not ride or ride.status != "searching":
            return {"error": "Заказ недоступен"}

        return self.ride_repo.update_status(db, ride_id, driver_id, "accepted")

