from pydantic import BaseModel


class age_rating_type(BaseModel):
    ageRaiting: int
    PGraiting: str = None
    minAge: int = None
    description: str  = None
