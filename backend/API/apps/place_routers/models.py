from sqlalchemy import Table, Column, ForeignKey, Integer, DateTime, VARCHAR, Float
from apps.repository import Base


class place_info(Base):
    __tablename__ = 'placeInfo'
    idPlace = Column(Integer, primary_key=True, nullable=True)
    placeType = Column(VARCHAR(50), nullable=True)

