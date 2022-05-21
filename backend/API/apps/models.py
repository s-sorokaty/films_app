from sqlalchemy import Table, Column, ForeignKey, Integer, DateTime, VARCHAR, Float
from sqlalchemy.orm import relationship
from repository import Base
from apps.client_routers.models import client_info
from apps.employee_routers.models import employee_info
from apps.film_info_routers.models import film_info
from apps.place_routers.models import place_info
from apps.hall_routers.models import hall_info


film_on_session = Table('filmOnSession', Base.metadata,
                        Column('idSession', ForeignKey(
                            'sessionInfo.idSession'), primary_key=True),
                        Column('idFilm', ForeignKey(
                            film_info.idFilm), primary_key=True)
                        )


class session_info(Base):
    __tablename__ = 'sessionInfo'
    idSession = Column(Integer, primary_key=True, nullable=True)
    idHall = Column(Integer, ForeignKey(
        hall_info.idHall), nullable=True)
    Date = Column(DateTime, nullable=True)
    startTime = Column(DateTime, nullable=True)
    endTime = Column(DateTime, nullable=True)
    children = relationship("ticketInfo")
    children = relationship("filmInfo", secondary=film_on_session)


class ticket_info(Base):
    __tablename__ = 'ticketInfo'
    idTransaction = Column(Integer, primary_key=True, nullable=True)
    idSession = Column(Integer, ForeignKey(
        'sessionInfo.idSession'), nullable=True)
    idClient = Column(Integer, ForeignKey(
        client_info.idClient), nullable=True)
    idEmployee = Column(Integer, ForeignKey(
        employee_info.idEmployee), nullable=True)
    idHall = Column(Integer, ForeignKey(
       hall_info.idHall), nullable=True)
    idPlace = Column(Integer, ForeignKey(
        place_info.idPlace), nullable=True)
    ticketCost = Column(Float, nullable=True)
    startTime = Column(DateTime, nullable=True)
    parent = relationship(client_info, back_populates="children")
    parent = relationship(employee_info, back_populates="children")
