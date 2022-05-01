
from sqlalchemy.orm import Session
import models
from db_settings import engine


models.Base.metadata.create_all(bind=engine)

with Session(engine) as session:
    def save_emotion_events():
        return "ok"
