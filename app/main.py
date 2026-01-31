from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.schemas.offer import OfferCreate, OfferResponse

from app.database import get_db, engine, Base
from app.schemas.ride import RideCreate
from app.services.ride_service import RideService
from . import crud, models, schemas

# Создаем таблицы при запуске (для начала)
Base.metadata.create_all(bind=engine)

app = FastAPI()
ride_service = RideService()

@app.post("/rides/create")
def request_ride(
    ride: RideCreate,
    passenger_id = 1,
    db: Session = Depends(get_db)  # Проверь, что это есть!
):
    # ВАЖНО: db должна быть первым или вторым аргументом здесь
    result = ride_service.create_new_ride(db, ride, passenger_id)
    return result

@app.post("/rides/{ride_id}/accept")
def accept_ride(ride_id: int, driver_id: int, db: Session = Depends(get_db)):
    # Вызываем сервис принятия заказа
    result = ride_service.accept_ride(db, ride_id, driver_id)
    return result

@app.get("/rides/available")
def get_available_rides(db: Session = Depends(get_db)):
    # Официант просит повара отдать список свободных заказов
    rides = ride_service.get_active_orders(db)
    return rides

# Водитель делает предложение
@app.post("/offers/", response_model=OfferResponse)
def make_offer(offer: OfferCreate, db: Session = Depends(get_db)):
    return crud.create_offer(db=db, offer_data=offer)

# Пассажир смотрит, кто и сколько предложил
@app.get("/rides/{ride_id}/offers", response_model=list[OfferResponse])
def get_ride_offers(ride_id: int, db: Session = Depends(get_db)):
    return crud.get_offers_for_ride(db, ride_id=ride_id)