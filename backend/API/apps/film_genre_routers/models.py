from sqlalchemy import Table, Column, ForeignKey, Integer, DateTime, VARCHAR, Float
from apps.repository import Base


class film_genre(Base):
    __tablename__ = 'filmGenre'
    idGenre = Column(Integer, primary_key=True, nullable=True)
    genreFilm = Column(Integer, nullable=True)
