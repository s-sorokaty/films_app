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
    db_film = db.query(models.film_film).filter(
        models.film_film.idfilm == film.idfilm).first()
    if type(db_film) == models.film_film:
        db.delete(db_film)
        db.commit()
        return "OK"
    else:
        raise None


def update_film(film, db):
    db_film = create_db_film(film)
    db.query(models.film_film).filter(
        models.film_film.idfilm == film.idfilm)\
        .update({'idfilm': db_film.idfilm,
                 'filmFilm': db_film.filmFilm
                 })
    db.commit()


def get_film(film, db):
    if film:
        return db.query(models.film_film).filter(
            models.film_film.idfilm == film.idfilm).first()
    else:
        return db.query(models.film_film).limit(5).all()
