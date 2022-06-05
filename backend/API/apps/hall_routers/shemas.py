from pydantic import BaseModel


class hall(BaseModel):
    idHall: int = None
    description: str = None

