from pydantic import BaseModel


class client(BaseModel):
    idClient: int
    Name: str = None
    Surname: str = None
    phoneNumber: int = None
