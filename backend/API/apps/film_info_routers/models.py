from sqlalchemy import Table, Column, ForeignKey, Integer, DateTime, VARCHAR, Float
from sqlalchemy.orm import relationship
from apps.repository import Base
from apps.age_rating_routers.models import age_rating_type
from apps.film_genre_routers.models import film_genre


class genre_on_film(Base):
    __tablename__ = 'genreOnFilm'
    idFilm = Column(Integer, ForeignKey('filmInfo.idFilm'), primary_key=True)
    idGenre = Column(Integer, ForeignKey(film_genre.idGenre), primary_key=True)
            

class film_info(Base):
    __tablename__ = 'filmInfo'
    idFilm = Column(Integer, primary_key=True, nullable=True)
    typeFilm = Column(VARCHAR(50), nullable=True)
    nameFilm = Column(VARCHAR(50), nullable=True)
    ageRaiting = Column(Integer, ForeignKey(
        age_rating_type.ageRaiting), nullable=True)
    countryFilm = Column(VARCHAR(50), nullable=True)
    description = Column(VARCHAR(255), nullable=True)
    # children = relationship(film_genre, secondary=genre_on_film)