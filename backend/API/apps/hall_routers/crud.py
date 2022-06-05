from sqlalchemy.orm import Session
from apps.hall_routers import shemas, models


def create_db_hall(hall):
    return models.hall_info(
        idHall=hall.idHall,
        description=hall.description
    )


def add_hall(hall, db):
    db_hall = create_db_hall(hall)
    db.add(db_hall)
    db.commit()
    db.refresh(db_hall)


def delete_hall(hall, db):
    db_hall = db.query(models.hall_info).filter(
        models.hall_info.idHall == hall.idHall,
        models.hall_info.idPlace == hall.idPlace).first()
    if type(db_hall) == models.hall_info:
        db.delete(db_hall)
        db.commit()
        return "OK"
    else:
        raise None


def update_hall(hall, db):
    db_hall = create_db_hall(hall)
    db.query(models.hall_info).filter(
        models.hall_info.idHall == hall.idHall)\
        .update({'idHall': db_hall.idHall,
                 'description': db_hall.description
                 })
    db.commit()


def get_hall(hall, db):
    query_db =  db.query(models.hall_info)
    for key in hall:
        if key[1]:
            print(getattr(models.hall_info, key[0]), key[1])
            query_db = query_db.filter(
                getattr(models.hall_info, key[0]) == key[1]
            )
    return query_db.all() 

def get_columns_descriptions(db):
    return db.query(models.hall_info).statement.columns.keys()
