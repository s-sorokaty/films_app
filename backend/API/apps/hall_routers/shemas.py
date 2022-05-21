from pydantic import BaseModel


class hall(BaseModel):
    idHall: int
    idPlace: int = None

