from sqlalchemy import Table, Column, ForeignKey, Integer, DateTime, VARCHAR, Float
from apps.repository import Base
from apps.hall_routers.models import hall_info

class place_info(Base):
    __tablename__ = 'placeInfo'
    idPlace = Column(Integer, primary_key=True, nullable=True)
    idHall = Column(Integer, ForeignKey(hall_info.idHall), nullable=True)
    placeType = Column(VARCHAR(50), nullable=True)

