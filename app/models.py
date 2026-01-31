# from sqlalchemy import Column, Integer, String, Float, ForeignKey
# from .database import Base
# from sqlalchemy.orm import relationship
# # from app.core.database import Base
#
# class RideModel(Base):
#     __tablename__ = "rides"
#     id = Column(Integer, primary_key=True)
#     pickup_location = Column(String) # убедись, что имя такое
#     destination = Column(String)
#     offered_price = Column(Float)
#
# class RideModel(Base):
#     __tablename__ = "rides"
#
#     id = Column(Integer, primary_key=True, index=True)
#     start_point = Column(String)
#     end_point = Column(String)
#     price = Column(Integer)
#     status = Column(String, default="searching") # searching, in_progress, completed
#     passenger_id = Column(Integer)
#     driver_id = Column(Integer, nullable=True) # Сначала пусто, пока водитель не нажмет "Принять"
#     offers = relationship("Offer", back_populates="ride")
#
# class Offer(Base):
#     __tablename__ = "offers"
#
#     id = Column(Integer, primary_key=True, index=True)
#     ride_id = Column(Integer, ForeignKey("rides.id")) # К какому заказу предложение
#     driver_name = Column(String) # Позже заменим на ID водителя
#     proposed_price = Column(Float)
#     status = Column(String, default="pending") # pending, accepted, rejected
#
#     # Связь: предложение принадлежит одной поездке
#     ride = relationship("Ride", back_populates="offers")

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship

class RideModel(Base):
    __tablename__ = "rides"

    id = Column(Integer, primary_key=True, index=True)
    start_point = Column(String)  # Было pickup_location
    end_point = Column(String)    # Было destination
    price = Column(Float)         # Было offered_price
    status = Column(String, default="searching")
    passenger_id = Column(Integer)
    driver_id = Column(Integer, nullable=True)

    # Связь с офферами (указываем имя класса 'Offer')
    offers = relationship("Offer", back_populates="ride")

class Offer(Base):
    __tablename__ = "offers"

    id = Column(Integer, primary_key=True, index=True)
    ride_id = Column(Integer, ForeignKey("rides.id"))
    driver_name = Column(String)
    proposed_price = Column(Float)
    status = Column(String, default="pending")

    # Связь с заказом (указываем имя класса 'RideModel')
    ride = relationship("RideModel", back_populates="offers")