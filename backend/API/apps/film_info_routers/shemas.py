from pydantic import BaseModel


class film(BaseModel):
    idFilm: int = None
    typeFilm: str = None
    nameFilm: str = None
    ageRaiting: int = None
    countryFilm: str = None
    description: str = None


class genre_on_film(BaseModel):
    idFilm: int = None
    idGenre: int = None