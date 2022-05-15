
from sqlalchemy.orm import Session
from db_settings import engine




with Session(engine) as session:
    def init():
        return "ok"
