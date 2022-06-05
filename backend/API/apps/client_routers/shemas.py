from pydantic import BaseModel


class client(BaseModel):
    idClient: int = None
    Name: str = None
    Surname: str = None
    phoneNumber: int = None
