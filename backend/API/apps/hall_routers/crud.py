from sqlalchemy.orm import Session
from apps.hall_routers import shemas, models

def create_db_hall(hall):
    return models.hall_info(
        idHall=hall.idHall,
        idPlace=hall.idPlace
    )


def add_hall(hall, db):
    print(hall)
    db_hall = create_db_hall(hall)
    db.add(db_hall)
    db.commit()
    db.refresh(db_hall)


def delete_hall(hall, db):
    db_hall = db.query(models.hall_info).filter(
        models.hall_info.idHall == hall.idHall).first()
    if type(db_hall) == models.hall_info:
        db.delete(db_hall)
        db.commit()
        return "OK"
    else:
        raise None


def update_hall(hall, db):
    db_hall = create_db_hall(hall)
    db.query(models.hall_info).filter(
        models.hall_info.idhall == hall.idhall)\
        .update({'idHall': db_hall.idHall,
                 'idhall': db_hall.idhall
                 })
    db.commit()


def get_hall(hall, db):
    if hall:
        return db.query(models.hall_info).filter(
            models.hall_info.idHall == hall.idHall).first()
    else:
        return db.query(models.hall_info).limit(5).all()

def get_columns_descriptions(db):
    return db.query(models.hall_info).statement.columns.keys()
