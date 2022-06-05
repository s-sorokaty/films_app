from pydantic import BaseModel


class age_rating_type(BaseModel):
    ageRaiting: int = None
    PGraiting: str = None
    minAge: int = None
    description: str  = None
