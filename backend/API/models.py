
from pymysql import Timestamp
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, JSON, VARCHAR, Float
from repository import Base
from db_settings import engine
from settings import get_settings

settings = get_settings()

class session_info(Base):
    __tablename__ = 'sessionInfo'
    idSession = Column(Integer, primary_key=True, nullable=True)
    idShowFilm = Column(Integer, nullable=True)
    idHall = Column(Integer, nullable=True)
    idPlace = Column(Integer, nullable=True)
    Date = Column(DateTime, nullable=True)
    startTime = Column(DateTime, nullable=True)
    endTime = Column(DateTime, nullable=True)  

class hall_info(Base):
    __tablename__ = 'hallInfo'
    idHall = Column(Integer, primary_key=True, nullable=True)
    Place = Column(Integer, nullable=True)

class film_on_session(Base):
    __tablename__ = 'filmOnSession'
    idShowFilm = Column(Integer, primary_key=True, nullable=True)
    idFilm = Column(Integer, nullable=True)

class film_info(Base):
    __tablename__ = 'filmInfo'
    idFilm = Column(Integer, primary_key=True, nullable=True)
    typeFilm = Column(VARCHAR(50), nullable=True)
    nameFilm = Column(VARCHAR(50), nullable=True)
    ageRating = Column(Integer, nullable=True)
    countryFilm = Column(VARCHAR(50), nullable=True)
    description = Column(VARCHAR(255), nullable=True)  

class age_rating_type(Base):
    __tablename__ = 'ageRatingType'
    agerRaiting = Column(Integer, primary_key=True, nullable=True)
    PGraiting = Column(VARCHAR(50), nullable=True)
    minAge = Column(Integer, nullable=True)
    description = Column(VARCHAR(255), nullable=True)  

class genre_on_film(Base):
    __tablename__ = 'genreOnFilm'
    idFilm = Column(Integer, primary_key=True, nullable=True)
    idGenre = Column(VARCHAR(50), nullable=True)

class film_types(Base):
    __tablename__ = 'filmTypes'
    idGenre = Column(Integer, primary_key=True, nullable=True)
    genreFilm = Column(Integer, primary_key=True, nullable=True)






class ticket_info(Base):
    __tablename__ = 'ticketInfo'
    idTransaction = Column(Integer, primary_key=True, nullable=True)
    idSession = Column(Integer, nullable=True)
    idClient = Column(Integer, nullable=True)
    idEmployee = Column(Integer, nullable=True)
    ticketCost = Column(Float, nullable=True)
    endDate = Column(DateTime, nullable=True)  

class client_info(Base):
    __tablename__ = 'clientInfo'
    idClient = Column(Integer, primary_key=True, nullable=True)
    Name = Column(VARCHAR(50), nullable=True)
    Surname = Column(VARCHAR(50), nullable=True) 
    phoneNumber = Column(Integer, nullable=True)

class employee_info(Base):
    __tablename__ = 'employeeInfo'
    idEmployee = Column(Integer, primary_key=True, nullable=True)
    Name = Column(VARCHAR(50), nullable=True)
    Surname = Column(VARCHAR(50), nullable=True) 
    phoneNumber = Column(Integer, nullable=True)