from pydantic import BaseModel


class employeer(BaseModel):
    idEmployee: int
    Name: str = None
    Surname: str = None
    phoneNumber: int = None
