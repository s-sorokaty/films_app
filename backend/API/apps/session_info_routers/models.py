from sqlalchemy import Table, Column, ForeignKey, Integer, DateTime, VARCHAR, Float
from sqlalchemy.orm import relationship
from apps.repository import Base
from apps.film_info_routers.models import film_info
from apps.hall_routers.models import hall_info


class film_on_session(Base):
    __tablename__ = 'filmOnSession'
    idSession = Column(Integer, ForeignKey('sessionInfo.idSession'), primary_key=True)
    idFilm = Column(Integer, ForeignKey(film_info.idFilm), primary_key=True)
     

class session_info(Base):
    __tablename__ = 'sessionInfo'
    idSession = Column(Integer, primary_key=True, nullable=True)
    idHall = Column(Integer, ForeignKey(
        hall_info.idHall), nullable=True)
    # Date = Column(DateTime, nullable=True)
    startTime = Column(DateTime, nullable=True)
    endTime = Column(DateTime, nullable=True)
    # children = relationship(film_info, secondary=film_on_session)
