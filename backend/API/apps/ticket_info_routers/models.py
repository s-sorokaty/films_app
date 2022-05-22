from sqlalchemy import Table, Column, ForeignKey, Integer, DateTime, VARCHAR, Float
from sqlalchemy.orm import relationship
from repository import Base
from apps.client_routers.models import client_info
from apps.employee_routers.models import employee_info
from apps.place_routers.models import place_info
from apps.hall_routers.models import hall_info
from apps.session_info_routers.models import session_info

class ticket_info(Base):
    __tablename__ = 'ticketInfo'
    idTransaction = Column(Integer, primary_key=True, nullable=True)
    idSession = Column(Integer, ForeignKey(
        session_info.idSession), nullable=True)
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
    parent = relationship(session_info)
    parent = relationship(client_info)
    parent = relationship(employee_info)
    