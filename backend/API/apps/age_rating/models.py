from sqlalchemy import Table, Column, ForeignKey, Integer, DateTime, VARCHAR, Float

from apps.repository import Base


class age_rating_type(Base):
    __tablename__ = 'ageRatingType'
    ageRaiting = Column(Integer, primary_key=True, nullable=True)
    PGraiting = Column(VARCHAR(50), nullable=True)
    minAge = Column(Integer, nullable=True)
    description = Column(VARCHAR(255), nullable=True)
