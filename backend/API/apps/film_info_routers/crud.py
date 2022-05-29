from sqlalchemy.orm import Session
from apps.film_info_routers import shemas, models


def create_db_film(film):
    return models.film_info(
        idfilm=film.idfilm,
        typeFilm=film.typeFilm,
        ageRating=film.ageRating,
        countryFilm=film.countryFilm,
        description=film.description,
        children=film.children
    )


def add_film(film, db):
    db_film = create_db_film(film)
    db.add(db_film)
    db.commit()
    db.refresh(db_film)


def delete_film(film, db):
    db_film = db.query(models.film_info).filter(
        models.film_info.idfilm == film.idfilm).first()
    if type(db_film) == models.film_info:
        db.delete(db_film)
        db.commit()
        return "OK"
    else:
        raise None


def update_film(film, db):
    db_film = create_db_film(film)
    db.query(models.film_info).filter(
        models.film_info.idfilm == film.idfilm)\
        .update({'idfilm': db_film.idfilm,
                 'filmFilm': db_film.filmFilm
                 })
    db.commit()


def get_film(film, db):
    if film:
        return db.query(models.film_info).filter(
            models.film_info.idfilm == film.idfilm).first()
    else:
        return db.query(models.film_info).limit(5).all()

def create_db_genre(genre):
    return models.genre_on_film(
        idFilm=genre.idFilm,
        idGenre=genre.typeFilm
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
    if genre:
        return db.query(models.genre_on_film).filter(
            models.genre_on_film.idFilm == genre.idFilm).first()
    else:
        return db.query(models.genre_on_film).limit(5).all()

def get_film_columns_descriptions(db):
    return db.query(models.film_info).statement.columns.keys()

def get_genre_columns_descriptions(db):
    return db.query(models.genre_on_film).statement.columns.keys()

