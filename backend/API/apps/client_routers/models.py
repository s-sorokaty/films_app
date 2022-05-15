from sqlalchemy import Table, Column, ForeignKey, Integer, DateTime, VARCHAR, Float

from apps.repository import Base





class client_info(Base):
    __tablename__ = 'clientInfo'
    idClient = Column(Integer, primary_key=True, nullable=True)
    Name = Column(VARCHAR(50), nullable=True)
    Surname = Column(VARCHAR(50), nullable=True)
    phoneNumber = Column(Integer, nullable=True)
