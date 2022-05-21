from sqlalchemy import Table, Column, ForeignKey, Integer, DateTime, VARCHAR, Float
from apps.repository import Base
from apps.place_routers.models import place_info


class hall_info(Base):
    __tablename__ = 'hallInfo'
    idHall = Column(Integer, primary_key=True, nullable=True)
    idPlace = Column(Integer, ForeignKey(place_info.idPlace), primary_key=True, nullable=True)
