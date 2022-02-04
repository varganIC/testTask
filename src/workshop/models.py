from .database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship


class CarModel(Base):
    __tablename__ = "car_model"

    id = Column(Integer, primary_key=True, autoincrement=True)
    brand = Column(String)

    child = relationship("Car", back_populates="owner", cascade="all, delete")


class Car(Base):
    __tablename__ = "car"

    id = Column(Integer, primary_key=True, autoincrement=True)
    driver = Column(String)
    number = Column(String, unique=True)
    year_release = Column(Date)
    color = Column(String)
    speed = Column(Integer)
    description = Column(String)
    owner_id = Column(Integer,  ForeignKey("car_model.id"))

    owner = relationship("CarModel", back_populates="child")





