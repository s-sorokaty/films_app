from pydantic import BaseModel


class place(BaseModel):
    idPlace: int = None
    placeType: str = None

