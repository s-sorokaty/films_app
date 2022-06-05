from sqlalchemy.orm import Session
from datetime import datetime
from apps.session_info_routers import shemas, models


def create_session_info(session_info):
    return models.session_info(
        idSession=session_info.idSession,
        idHall=session_info.idHall,
        startTime=datetime.fromtimestamp(session_info.startTime) ,
        endTime=datetime.fromtimestamp(session_info.endTime),
    )

def add_session_info(session_info, db):
    db_session_info = create_session_info(session_info)
    db.add(db_session_info)
    db.commit()
    db.refresh(db_session_info)


def delete_session_info(session_info, db):
    db_session_info = db.query(models.session_info).filter(
        models.session_info.idSession == session_info.idSession).first()
    if type(db_session_info) == models.session_info:
        db.delete(db_session_info)
        db.commit()
        return "OK"
    else:
        raise None


def update_session_info(session_info, db):
    db_place = create_session_info(session_info)
    db.query(models.session_info).filter(
        models.session_info.idSession == session_info.idSession)\
        .update({'idSession': db_place.idSession,
                'idHall':db_place.idHall,
                 'Date': db_place.Date,
                 'startTime': db_place.startTime,
                 'endTime': db_place.endTime,
                 })
    db.commit()


def get_session_info(session_info, db):
    query_db =  db.query(models.session_info)
    for key in session_info:
        if key[1]:
            print(getattr(models.session_info, key[0]), key[1])
            query_db = query_db.filter(
                getattr(models.session_info, key[0]) == key[1]
            )
    return query_db.all() 
    
def get_columns_descriptions_session_info(db):
    return db.query(models.session_info).statement.columns.keys()



def create_film_on_session(film_session):
    return models.film_on_session(
        idSession=film_session.idSession,
        idFilm=film_session.idFilm,
    )

def add_film_on_session(film_on_session, db):
    db_film_on_session = create_film_on_session(film_on_session)
    db.add(db_film_on_session)
    db.commit()
    db.refresh(db_film_on_session)


def delete_film_on_session(film_on_session, db):
    db_film_on_session = db.query(models.film_on_session).filter(
        models.film_on_session.idSession == film_on_session.idSession).first()
    if type(db_film_on_session) == models.film_on_session:
        db.delete(db_film_on_session)
        db.commit()
        return "OK"
    else:
        raise None


def update_film_on_session(film_on_session, db):
    db_film_on_session = create_film_on_session(film_on_session)
    db.query(models.film_on_session).filter(
        models.film_on_session.idSession == film_on_session.idSession)\
        .update({'idSession': db_film_on_session.idSession,
                'idFilm':db_film_on_session.idFilm,
                 })
    db.commit()


def get_film_on_session(film_on_session, db):
    query_db =  db.query(models.film_on_session)
    for key in film_on_session:
        if key[1]:
            query_db = query_db.filter(
                getattr(models.film_on_session, key[0]) == key[1]
            )
    return query_db.all() 
    
def get_columns_descriptions_film_on_session(db):
    return db.query(models.film_on_session).statement.columns.keys()
