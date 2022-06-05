from sqlalchemy.orm import Session
from apps.film_info_routers import shemas, models


def create_db_film(film):
    return models.film_info(
        idFilm=film.idFilm,
        typeFilm=film.typeFilm,
        nameFilm=film.nameFilm,
        ageRaiting=film.ageRaiting,
        countryFilm=film.countryFilm,
        description=film.description,
    )


def add_film(film, db):
    db_film = create_db_film(film)
    db.add(db_film)
    db.commit()
    db.refresh(db_film)


def delete_film(film, db):
    db_film = db.query(models.film_info).filter(
        models.film_info.idFilm == film.idFilm).first()
    if type(db_film) == models.film_info:
        db.delete(db_film)
        db.commit()
        return "OK"
    else:
        raise None


def update_film(film, db):
    db_film = create_db_film(film)
    db.query(models.film_info).filter(
        models.film_info.idFilm == film.idFilm)\
        .update({'idFilm': db_film.idFilm,
                 'typeFilm': db_film.typeFilm,
                 'nameFilm': db_film.nameFilm,
                 'ageRaiting': db_film.ageRaiting,
                 'countryFilm': db_film.countryFilm,
                 'description': db_film.description,
                 })
    db.commit()


def get_film(film, db):
    query_db =  db.query(models.film_info)
    for key in film:
        if key[1]:
            print(getattr(models.film_info, key[0]), key[1])
            query_db = query_db.filter(
                getattr(models.film_info, key[0]) == key[1]
            )
    return query_db.all() 

def create_db_genre(genre):
    return models.genre_on_film(
        idFilm=genre.idFilm,
        idGenre=genre.idGenre
    )


def add_genre(genre, db):
    db_genre = create_db_genre(genre)
    db.add(db_genre)
    db.commit()
    db.refresh(db_genre)


def delete_genre(genre, db):
    db_genre = db.query(models.genre_on_film).filter(
        models.genre_on_film.idFilm == genre.idFilm).first()
    if type(db_genre) == models.film_info:
        db.delete(db_genre)
        db.commit()
        return "OK"
    else:
        raise None


def update_genre(genre, db):
    db_genre = create_db_genre(genre)
    db.query(models.genre_on_film).filter(
        models.genre_on_film.idFilm == genre.idFilm)\
        .update({'idFilm': genre.idFilm,
                 'idGenre': genre.idGenre
                 })
    db.commit()


def get_genre(genre, db):
    query_db =  db.query(models.genre_on_film)
    for key in genre:
        if key[1]:
            print(getattr(models.genre_on_film, key[0]), key[1])
            query_db = query_db.filter(
                getattr(models.genre_on_film, key[0]) == key[1]
            )
    return query_db.all() 

def get_film_columns_descriptions(db):
    return db.query(models.film_info).statement.columns.keys()

def get_genre_columns_descriptions(db):
    return db.query(models.genre_on_film).statement.columns.keys()

