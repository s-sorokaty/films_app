from fastapi import FastAPI, Response, Request
from settings import get_settings
import routers as psql_routers
from apps.employee_routers.routers import router as employee_routers
from apps.client_routers.routers import router as client_routers
from apps.age_rating_routers.routers import router as age_rating_routers
from apps.film_genre_routers.routers import router as film_genre_routers
from apps.film_info_routers.routers import router as film_info_routers
from apps.place_routers.routers import router as place_routers

print(get_settings())
print(psql_routers.init())

app = FastAPI()

app.include_router(employee_routers, prefix="/employee", tags=["employee"])
app.include_router(client_routers, prefix="/client", tags=["client"])
app.include_router(age_rating_routers,
                   prefix="/age-raiting", tags=["age-raiting"])
app.include_router(film_genre_routers, prefix="/film-genre", tags=["film-genre"])
app.include_router(film_info_routers, prefix="/film-info", tags=["film-info"])
app.include_router(place_routers, prefix="/place", tags=["place"])