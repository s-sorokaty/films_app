from sqlalchemy.orm import Session
from apps.client_routers import crud as users_crud
from apps.employee_routers import crud as employee_crud
from apps.film_genre_routers import crud as genre_crud
from apps.age_rating_routers import crud as age_rating_crud
from apps.film_info_routers import crud as film_crud
from apps.ticket_info_routers import crud as ticket_crud
from apps.film_info_routers import crud as film_info_crud
from apps.session_info_routers import crud as session_info_crud
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import pandas as pd


def generate_users_pdf(db):
    c = Canvas("reports/users.pdf")
    users = users_crud.get_client([], db)
    pdfmetrics.registerFont(TTFont('FreeSans', 'FreeSans.ttf'))
    c.setFont(psfontname='FreeSans', size=14)
    c.drawCentredString(250, 800, 'Клиенты')
    height = 700
    c.drawString(100, height+15, 'ID')
    c.drawString(150, height+15, 'Имя')
    c.drawString(300, height+15, 'Фамилия')
    c.drawString(500, height+15, 'Номер')
    for obj in users:
        c.drawString(100, height, str(obj.idClient))
        c.drawString(150, height, str(obj.Name))
        c.drawString(300, height, str(obj.Surname))
        c.drawString(500, height, str(obj.phoneNumber))
        height -= 15
    c.save()
    return 'OK'


def generate_employee_pdf(db):
    c = Canvas("reports/employee.pdf")
    employee = employee_crud.get_employee([], db)
    pdfmetrics.registerFont(TTFont('FreeSans', 'FreeSans.ttf'))
    c.setFont(psfontname='FreeSans', size=14)
    height = 700
    c.drawString(100, height+15, 'ID')
    c.drawString(150, height+15, 'Имя')
    c.drawString(300, height+15, 'Фамилия')
    c.drawString(500, height+15, 'Номер')
    c.drawString(250, 800, 'Сотрудники')
    for obj in employee:
        c.drawString(100, height, str(obj.idEmployee))
        c.drawString(150, height, str(obj.Name))
        c.drawString(300, height, str(obj.Surname))
        c.drawString(500, height, str(obj.phoneNumber))
        height -= 15
    c.save()
    return "OK"


def generate_genre_pdf(db):
    c = Canvas("reports/genre.pdf")
    genre = genre_crud.get_genre([], db)
    genre_on_film = film_crud.get_genre([], db)
    genre_on_film_df = pd.DataFrame([o.__dict__ for o in genre_on_film])
    pdfmetrics.registerFont(TTFont('FreeSans', 'FreeSans.ttf'))
    c.setFont(psfontname='FreeSans', size=14)
    height = 700
    c.drawString(250, 800, 'Жанры')
    c.drawString(100, height+50, 'ID жанра')
    c.drawString(250, height+50, 'Название жанра')
    c.drawString(400, height+50, 'Кол-во фильмов по жанрам')
    for obj in genre:
        c.drawString(100, height, str(obj.idGenre))
        c.drawString(250, height, str(obj.genreFilm))
        c.drawString(400, height, str(
            len(film_crud.get_genre([('idGenre', obj.idGenre)], db))))
        height -= 15
    c.save()
    return "OK"


def generate_film_pdf(db):
    c = Canvas("reports/film.pdf")
    pdfmetrics.registerFont(TTFont('FreeSans', 'FreeSans.ttf'))
    c.setFont(psfontname='FreeSans', size=12)
    film_data = film_crud.get_film([], db)
    age_rating_data = age_rating_crud.get_age_raiting([], db)
    genre_on_film = film_info_crud.get_genre([], db)
    genre_info = genre_crud.get_genre([], db)
    film_df = pd.DataFrame([o.__dict__ for o in film_data])
    age_rating_df = pd.DataFrame([o.__dict__ for o in age_rating_data])
    genre_on_film_df = pd.DataFrame([o.__dict__ for o in genre_on_film])
    genre_info_df = pd.DataFrame([o.__dict__ for o in genre_info])
    film_df = film_df.merge(
        age_rating_df, left_on='ageRaiting', right_on='ageRaiting')
    film_df = film_df[['idFilm', 'nameFilm', 'typeFilm', 'countryFilm',
                       'minAge', 'PGraiting', 'description_y', 'description_x', ]]
    film_df = film_df.merge(
        genre_on_film_df, left_on='idFilm', right_on='idFilm')
    film_df = film_df.merge(
        genre_info_df, left_on='idGenre', right_on='idGenre')

    height = 700

    c.drawString(250, 800, 'Фильмы')
    c.drawString(50, height+50, 'ID')
    c.drawString(70, height+50, 'Название')
    c.drawString(140, height+50, 'Тип')
    c.drawString(250, height+50, 'Жанр')
    c.drawString(300, height+50, 'Страна')
    c.drawString(350, height+50, 'Ограничение')
    c.drawString(450, height+50, 'Описание рейтинга')
    for obj in film_df.iterrows():
        c.drawString(50, height, str(obj[1].idFilm))
        c.drawString(70, height, str(obj[1].nameFilm))
        c.drawString(140, height, str(obj[1].typeFilm))
        c.drawString(250, height, str(obj[1].genreFilm))
        c.drawString(300, height, str(obj[1].countryFilm))
        c.drawString(370, height-7, str(obj[1].minAge))
        c.drawString(370, height+7, str(obj[1].PGraiting))
        c.drawString(450, height, str(obj[1].description_y))
        height -= 30
    c.save()
    return "OK"


def generate_ticket_pdf(db):
    c = Canvas("reports/ticket.pdf")
    pdfmetrics.registerFont(TTFont('FreeSans', 'FreeSans.ttf'))
    c.setFont(psfontname='FreeSans', size=12)
    user_data = users_crud.get_client([], db)
    employee_data = employee_crud.get_employee([], db)
    ticket_data = ticket_crud.get_ticket([], db)
    user_df = pd.DataFrame([o.__dict__ for o in user_data])
    employee_df = pd.DataFrame([o.__dict__ for o in employee_data])
    ticket_df = pd.DataFrame([o.__dict__ for o in ticket_data])
    ticket_df = ticket_df.merge(
        user_df, left_on='idClient', right_on='idClient')
    ticket_df = ticket_df[['idTransaction', 'idSession', 'idEmployee',
                           'ticketCost', 'startTime', 'Name', 'Surname', 'phoneNumber']]
    ticket_df = ticket_df.merge(
        employee_df, left_on='idEmployee', right_on='idEmployee')
    ticket_df = ticket_df[['idTransaction', 'idSession', 'ticketCost', 'startTime',
                           'Name_x', 'Surname_x', 'phoneNumber_x', 'Name_y', 'Surname_y', 'phoneNumber_y']]

    c.drawString(250, 800, 'Билеты')
    height = 700
    c.drawString(50, height+40, 'ID')
    c.drawString(70, height+40, 'Цена')
    c.drawString(120, height+40, 'Дата продажи')
    c.drawString(250, height+40, 'Фильмы')
    c.drawString(400, height+40, 'Клиент')
    c.drawString(500, height+40, 'Сотрудник')
    for obj in ticket_df.iterrows():
        c.drawString(50, height, str(obj[1].idTransaction))
        c.drawString(70, height, str(obj[1].ticketCost))
        c.drawString(120, height, str(obj[1].startTime))
        res = session_info_crud.get_film_on_session(
            [('idSession', obj[1].idSession)], db)
        margin = 0
        for film in res:
            f = film_info_crud.get_film([('idFilm', film.idFilm)], db)
            c.drawString(250, height-10 + margin, str(f[0].nameFilm))
            margin += 15
        c.drawString(400, height, str(obj[1].Name_x))
        c.drawString(400, height-15, str(obj[1].Surname_x))
        c.drawString(400, height+15, str(obj[1].phoneNumber_x))
        c.drawString(500, height, str(obj[1].Name_y))
        c.drawString(500, height-15, str(obj[1].Surname_y))
        c.drawString(500, height+15, str(obj[1].phoneNumber_y))
        height -= 50
    c.save()
    return "OK"


def generate_session_pdf(db):
    c = Canvas("reports/session.pdf")
    pdfmetrics.registerFont(TTFont('FreeSans', 'FreeSans.ttf'))
    c.setFont(psfontname='FreeSans', size=12)
    session_data = session_info_crud.get_session_info([], db)
    session_df = pd.DataFrame([o.__dict__ for o in session_data])
    height = 700
    c.drawString(50, height+50, 'ID сессии')
    c.drawString(150, height+50,'Начало')
    c.drawString(300, height+50,'Конец')
    c.drawString(250, 800, 'Сессии')
    for obj in session_df.iterrows():
        c.drawString(50, height, str(obj[1].idSession))
        c.drawString(150, height, str(obj[1].startTime))
        c.drawString(300, height, str(obj[1].endTime))

        height -= 15
    c.save()
    return "OK"
