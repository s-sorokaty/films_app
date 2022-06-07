from sqlalchemy import Table, Column, ForeignKey, Integer, DateTime, VARCHAR, Float, BigInteger
from apps.repository import Base


class employee_info(Base):
    __tablename__ = 'employeeInfo'
    idEmployee = Column(Integer, primary_key=True, nullable=True)
    Name = Column(VARCHAR(50), nullable=True)
    Surname = Column(VARCHAR(50), nullable=True)
    phoneNumber = Column(BigInteger, nullable=True)
