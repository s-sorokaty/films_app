from sqlalchemy.orm import Session
from apps.film_genre_routers import shemas, models


def create_db_emploeer(genre):
    return models.film_genre(
        idGenre=genre.idGenre,
        genreFilm=genre.genreFilm
    )


def add_genre(genre, db):
    db_genre = create_db_emploeer(genre)
    db.add(db_genre)
    db.commit()
    db.refresh(db_genre)


def delete_genre(genre, db):
    db_genre = db.query(models.film_genre).filter(
        models.film_genre.idGenre == genre.idGenre).first()
    if type(db_genre) == models.film_genre:
        db.delete(db_genre)
        db.commit()
        return True
    else:
        raise False


def update_genre(genre, db):
    db_genre = create_db_emploeer(genre)
    db.query(models.film_genre).filter(
        models.film_genre.idGenre == genre.idGenre)\
        .update({'idGenre': db_genre.idGenre,
                 'Name': db_genre.Name,
                 'Surname': db_genre.Surname,
                 'phoneNumber': db_genre.phoneNumber
                 })
    db.commit()


def get_genre(genre, min, max, db):
    if genre:
        return db.query(models.film_genre).filter(
            models.film_genre.idGenre == genre.idGenre).first()
    else:
        return db.query(models.film_genre).filter(
            models.film_genre.idGenre >= min, models.film_genre.idGenre <= max).limit(5).all()
