from pydantic import BaseModel


class genre(BaseModel):
    idGenre: int
    genreFilm: str = None
