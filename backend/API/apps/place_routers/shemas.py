from pydantic import BaseModel


class place(BaseModel):
    idPlace: int
    placeType: str = None

