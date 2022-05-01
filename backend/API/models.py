from sqlalchemy import Table, Column, ForeignKey, Integer, DateTime, VARCHAR, Float
from sqlalchemy.orm import relationship
from repository import Base

from settings import get_settings


settings = get_settings()


class client_info(Base):
    __tablename__ = 'clientInfo'
    idClient = Column(Integer, primary_key=True, nullable=True)
    Name = Column(VARCHAR(50), nullable=True)
    Surname = Column(VARCHAR(50), nullable=True)
    phoneNumber = Column(Integer, nullable=True)
    children = relationship("ticketInfo")


class employee_info(Base):
    __tablename__ = 'employeeInfo'
    idEmployee = Column(Integer, primary_key=True, nullable=True)
    Name = Column(VARCHAR(50), nullable=True)
    Surname = Column(VARCHAR(50), nullable=True)
    phoneNumber = Column(Integer, nullable=True)
    children = relationship("ticketInfo")


class film_types(Base):
    __tablename__ = 'filmTypes'
    idGenre = Column(Integer, primary_key=True, nullable=True)
    genreFilm = Column(Integer, nullable=True)


class age_rating_type(Base):
    __tablename__ = 'ageRatingType'
    agerRaiting = Column(Integer, primary_key=True, nullable=True)
    PGraiting = Column(VARCHAR(50), nullable=True)
    minAge = Column(Integer, nullable=True)
    description = Column(VARCHAR(255), nullable=True)


class hall_info(Base):
    __tablename__ = 'hallInfo'
    idHall = Column(Integer, primary_key=True, nullable=True)
    idPlace = Column(Integer, ForeignKey('placeInfo.idPlace'), nullable=True)


class place_info(Base):
    __tablename__ = 'placeInfo'
    idPlace = Column(Integer, primary_key=True, nullable=True)
    placeType = Column(VARCHAR(50), nullable=True)


genre_on_film = Table('genreOnFilm', Base.metadata,
                      Column('idFilm', ForeignKey('filmInfo.idFilm')),
                      Column('idGenre', ForeignKey('filmTypes.idGenre'))
                      )


class film_info(Base):
    __tablename__ = 'filmInfo'
    idFilm = Column(Integer, primary_key=True, nullable=True)
    typeFilm = Column(VARCHAR(50), nullable=True)
    nameFilm = Column(VARCHAR(50), nullable=True)
    ageRating = Column(Integer, ForeignKey(
        'ageRatingType.agerRaiting'), nullable=True)
    countryFilm = Column(VARCHAR(50), nullable=True)
    description = Column(VARCHAR(255), nullable=True)
    children = relationship("filmTypes", secondary=genre_on_film)


film_on_session = Table('filmOnSession', Base.metadata,
                        Column('idSession', ForeignKey(
                            'sessionInfo.idSession')),
                        Column('idFilm', ForeignKey('filmInfo.idFilm'))
                        )


class session_info(Base):
    __tablename__ = 'sessionInfo'
    idSession = Column(Integer, primary_key=True, nullable=True)
    idHall = Column(Integer, ForeignKey(
        'hallInfo.idHall'), nullable=True)
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
        'clientInfo.idClient'), nullable=True)
    idEmployee = Column(Integer, ForeignKey(
        'employeeInfo.idEmployee'), nullable=True)
    idHall = Column(Integer, ForeignKey(
        'hallInfo.idHall'), nullable=True)
    idPlace = Column(Integer, ForeignKey(
        'placeInfo.idPlace'), nullable=True)
    ticketCost = Column(Float, nullable=True)
    startTime = Column(DateTime, nullable=True)
