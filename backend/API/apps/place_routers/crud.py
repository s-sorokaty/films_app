from sqlalchemy.orm import Session
from apps.place_routers import shemas, models


def create_db_place(place):
    return models.place_info(
        idPlace=place.idPlace,
        placeType=place.placeType
    )


def add_place(place, db):
    db_place = create_db_place(place)
    db.add(db_place)
    db.commit()
    db.refresh(db_place)


def delete_place(place, db):
    db_place = db.query(models.place_info).filter(
        models.place_info.idPlace == place.idPlace).first()
    if type(db_place) == models.place_info:
        db.delete(db_place)
        db.commit()
        return "OK"
    else:
        raise None


def update_place(place, db):
    db_place = create_db_place(place)
    db.query(models.place_info).filter(
        models.place_info.idPlace == place.idPlace)\
        .update({'idPlace': db_place.idPlace,
                 'placeType': db_place.placeType
                 })
    db.commit()


def get_place(place, db):
    if place:
        return db.query(models.place_info).filter(
            models.place_info.idPlace == place.idPlace).first()
    else:
        return db.query(models.place_info).limit(5).all()

def get_columns_descriptions(db):
    return db.query(models.place_info).statement.columns.keys()
