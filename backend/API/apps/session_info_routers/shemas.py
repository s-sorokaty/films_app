from pydantic import BaseModel


class place(BaseModel):
    idPlace: int = None
    idHall: int = None
    placeType: str = None

