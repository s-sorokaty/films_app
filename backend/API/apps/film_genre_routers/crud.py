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
        return "OK"
    else:
        raise None


def update_genre(genre, db):
    db_genre = create_db_emploeer(genre)
    db.query(models.film_genre).filter(
        models.film_genre.idGenre == genre.idGenre)\
        .update({'idGenre': db_genre.idGenre,
                 'genreFilm': db_genre.genreFilm
                 })
    db.commit()


def get_genre(genre, db):
    query_db =  db.query(models.film_genre)
    for key in genre:
        if key[1]:
            print(getattr(models.film_genre, key[0]), key[1])
            query_db = query_db.filter(
                getattr(models.film_genre, key[0]) == key[1]
            )
    return query_db.all()

def get_columns_descriptions(db):
    return db.query(models.film_genre).statement.columns.keys()
