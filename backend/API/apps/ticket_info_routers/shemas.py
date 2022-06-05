from datetime import datetime
from pydantic import BaseModel

class ticket(BaseModel):
    idTransaction: int = None
    idSession: int = None
    idClient: int = None
    idEmployee: int = None
    idHall: int = None
    idPlace: int = None
    ticketCost: float = None
    startTime: datetime = None
