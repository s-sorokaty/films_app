
from sqlalchemy.orm import Session
from db_settings import engine
from apps.client_routers import models as client_models
from apps.employee_routers import models as employee__models
from apps import models as all_models


client_models.Base.metadata.create_all(bind=engine)
employee__models.Base.metadata.create_all(bind=engine)
all_models.Base.metadata.create_all(bind=engine)

with Session(engine) as session:
    def init():
        return "ok"
