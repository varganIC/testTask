from typing import List, Optional

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine
from .create_db import ConectionDB

connect_to_db = ConectionDB()

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/cars/show", response_model=List[schemas.Car])
def read_car(number_car: str, db: Session = Depends(get_db)):
    cars = crud.get_car(db, number=number_car)
    return cars


@app.get("/car_model/show", response_model=schemas.CarModel)
def read_model_cars(model_id: int, db: Session = Depends(get_db)):
    cars = crud.get_models(db, model_id=model_id)
    return cars


@app.post("/cars/create", response_model=schemas.Car)
def create_car(car: schemas.Car, db: Session = Depends(get_db)):
    return crud.create_car(db=db, car=car)


@app.post("/car_model/", response_model=schemas.CarModel)
def create_model_car(car_model: schemas.CarModel, db: Session = Depends(get_db)):
    return crud.create_car_model(db=db, car_model=car_model)


@app.delete("/cars/delete", response_model=schemas.Car)
def delete_car(car_id: int, db: Session = Depends(get_db)):
    return crud.delete_car(db=db, car_id=car_id)


@app.delete("/car_model/delete", response_model=Optional[schemas.CarModel])
def delete_car_model(car_model_id: int, db: Session = Depends(get_db)):
    return crud.delete_car_model(db=db, car_model_id=car_model_id)