from sqlalchemy.orm import Session
from apps.hall_routers import shemas, models

def create_db_place(place):
    return models.hall_info(
        idHall=place.idHall,
        idPlace=place.idPlace
    )


def add_place(place, db):
    db_place = create_db_place(place)
    db.add(db_place)
    db.commit()
    db.refresh(db_place)


def delete_place(place, db):
    db_place = db.query(models.hall_info).filter(
        models.hall_info.idHall == place.idHall).first()
    if type(db_place) == models.hall_info:
        db.delete(db_place)
        db.commit()
        return "OK"
    else:
        raise None


def update_place(place, db):
    db_place = create_db_place(place)
    db.query(models.hall_info).filter(
        models.hall_info.idPlace == place.idPlace)\
        .update({'idHall': db_place.idHall,
                 'idPlace': db_place.idPlace
                 })
    db.commit()


def get_place(place, db):
    if place:
        return db.query(models.hall_info).filter(
            models.hall_info.idHall == place.idHall).first()
    else:
        return db.query(models.hall_info).limit(5).all()

def get_columns_descriptions(db):
    return db.query(models.hall_info).statement.columns.keys()
