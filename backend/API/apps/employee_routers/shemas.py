from pydantic import BaseModel


class employeer(BaseModel):
    idEmployee: int = None
    Name: str = None
    Surname: str = None
    phoneNumber: int = None
