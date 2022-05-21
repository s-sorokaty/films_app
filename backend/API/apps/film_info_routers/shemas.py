from pydantic import BaseModel


class film(BaseModel):
    idFilm: int
    typeFilm: str = None
    nameFilm: str = None
    ageRating: int = None
    countryFilm: str = None
    description: str = None


class genre_on_film(BaseModel):
    idFilm: int
    idGenre: int