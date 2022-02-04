from sqlalchemy.orm import Session
from . import models, schemas


def get_models(db: Session, model_id: int):
    return db.query(models.CarModel).get(model_id)


def get_car(db: Session, number: str):
    search = '{}%'.format(number)
    db_car = db.query(models.Car).filter(models.Car.number.like(search)).all()
    return db_car


def create_car_model(db: Session, car_model: schemas.CarModel):
    db_car_model = models.CarModel(id=car_model.id, brand=car_model.brand)
    db.add(db_car_model)
    db.commit()
    db.refresh(db_car_model)
    return db_car_model


def create_car(db: Session, car: schemas.Car):
    db_car = models.Car(
        id=car.id,
        driver=car.driver,
        number=car.number,
        year_release=car.year_release,
        color=car.color,
        speed=car.speed,
        description=car.description,
        owner_id=car.owner_id
    )
    db.add(db_car)
    db.commit()
    db.refresh(db_car)
    return db_car


def delete_car(db: Session, car_id: int):
    db_car = db.query(models.Car).filter(models.Car.id == car_id).one()
    db.delete(db_car)
    db.commit()
    return db_car


def delete_car_model(db: Session, car_model_id: int):
    db_car_model = db.query(models.CarModel).filter(models.CarModel.id == car_model_id).one()
    db.delete(db_car_model)
    db.commit()
    # db_car_model = db.query(models.Car).filter(models.Car.owner_id == car_model_id).all()
    # db.delete(db_car_model)
    # db.commit()
    return db_car_model

