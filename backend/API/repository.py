from sqlalchemy.ext.declarative import declarative_base
from db_settings import engine
from sqlalchemy.orm import sessionmaker


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()