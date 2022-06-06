from pydantic import BaseModel
from datetime import datetime

class film_on_session(BaseModel):
    idSession: int = None
    idFilm: int = None


class session_info(BaseModel):
    idSession: int = None
    idHall: int = None
    # Date: int = None
    startTime: datetime = None
    endTime: datetime = None
