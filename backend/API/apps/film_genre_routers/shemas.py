from pydantic import BaseModel


class genre(BaseModel):
    idGenre: int = None
    genreFilm: str = None
