from pydantic import BaseModel


class film(BaseModel):
    idFilm: int
    typeFilm: str = None
    nameFilm: str = None
    ageRating: int = None
    countryFilm: str = None
    description: str = None