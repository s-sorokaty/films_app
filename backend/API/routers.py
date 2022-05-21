
from sqlalchemy.orm import Session
from db_settings import engine
from apps.client_routers import models as client_models
from apps.employee_routers import models as employee__models
from apps.age_rating_routers import models as age_rating_models
from apps.film_info_routers import models as film_info_models
from apps.film_genre_routers import models as film_genre_models
from apps.place_routers import models as place_models
from apps.hall_routers  import models as hall_models
from apps import models as all_models


client_models.Base.metadata.create_all(bind=engine) 
employee__models.Base.metadata.create_all(bind=engine)
age_rating_models.Base.metadata.create_all(bind=engine)
film_info_models.Base.metadata.create_all(bind=engine)
film_genre_models.Base.metadata.create_all(bind=engine)
place_models.Base.metadata.create_all(bind=engine)
hall_models.Base.metadata.create_all(bind=engine)
all_models.Base.metadata.create_all(bind=engine)

with Session(engine) as session:
    def init():
        return "ok"
