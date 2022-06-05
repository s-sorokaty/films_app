from sqlalchemy import Table, Column, ForeignKey, Integer, DateTime, VARCHAR, Float
from apps.repository import Base


class hall_info(Base):
    __tablename__ = 'hallInfo'
    idHall = Column(Integer, primary_key=True, nullable=True)
    description = Column(VARCHAR(255), nullable=True)
