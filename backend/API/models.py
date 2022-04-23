
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, JSON, VARCHAR
from repository import Base
from db_settings import engine
from settings import get_settings

settings = get_settings()

class emotion_events(Base):
    __tablename__ = 'test'
    id = Column(VARCHAR(50), primary_key=True, nullable=True)
    device_id = Column(VARCHAR(50), nullable=True)
    user_id = Column(VARCHAR(50), nullable=True)
    player_name = Column(VARCHAR(50), nullable=True)
    event = Column(VARCHAR(32), nullable=True)
    event_time = Column(DateTime, nullable=True)  
