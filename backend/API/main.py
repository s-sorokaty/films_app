from fastapi import FastAPI, Response, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates

from apps.employee_routers.routers import router as employee_routers
from apps.client_routers.routers import router as client_routers
from apps.age_rating_routers.routers import router as age_rating_routers
from apps.film_genre_routers.routers import router as film_genre_routers
from apps.film_info_routers.routers import router as film_info_routers
from apps.place_routers.routers import router as place_routers
from apps.hall_routers.routers import router as hall_routers
from apps.ticket_info_routers.routers import router as ticket_info_routers


import routers as psql_db

psql_db.init()
templates = Jinja2Templates(directory="templates")

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get(path='/main', response_class=HTMLResponse)
def get_main_page(request: Request):
    return templates.TemplateResponse('index.html', {"request": request})


@app.get(path='/api', response_class=HTMLResponse)
def get_api(request: Request):
    return templates.TemplateResponse('/api.js', {"request": request})


@app.get(path='/js', response_class=HTMLResponse)
def get_main_script(request: Request):
    return templates.TemplateResponse('/main.js', {"request": request})


app.include_router(employee_routers, prefix="/employee", tags=["employee"])
app.include_router(hall_routers, prefix="/hall", tags=["hall_routers"])
app.include_router(client_routers, prefix="/client", tags=["client"])
app.include_router(age_rating_routers,
                   prefix="/age-raiting", tags=["age-raiting"])
app.include_router(film_genre_routers, prefix="/film-genre",
                   tags=["film-genre"])
app.include_router(film_info_routers, prefix="/film-info", tags=["film-info"])
app.include_router(place_routers, prefix="/place", tags=["place"])
app.include_router(ticket_info_routers,
                   prefix="/ticket-info", tags=["ticket-info"])
