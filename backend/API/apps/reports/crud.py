from sqlalchemy.orm import Session
from apps.client_routers import crud as users_crud
from apps.employee_routers import crud as employee_crud
from apps.film_genre_routers import crud as genre_crud
from apps.age_rating_routers import crud as age_rating_crud
from apps.film_info_routers import crud as film_crud
from apps.ticket_info_routers import crud as ticket_crud
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import pandas as pd


def generate_users_pdf(db):
    c = Canvas("reports/users.pdf")
    users = users_crud.get_client([], db)
    pdfmetrics.registerFont(TTFont('FreeSans', 'FreeSans.ttf'))
    c.setFont(psfontname = 'FreeSans', size = 14)
    c.drawCentredString(250, 800,'Клиенты')
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
    c.setFont(psfontname = 'FreeSans', size = 14)
    height = 700
    c.drawString(100, height+15, 'ID')
    c.drawString(150, height+15, 'Имя')
    c.drawString(300, height+15, 'Фамилия')
    c.drawString(500, height+15, 'Номер')
    c.drawString(250, 800,'Сотрудники')
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
    pdfmetrics.registerFont(TTFont('FreeSans', 'FreeSans.ttf'))
    c.setFont(psfontname = 'FreeSans', size = 14)
    height = 700
    c.drawString(250, 800,'Жанры')
    for obj in genre:
         c.drawString(100, height, str(obj.idGenre))
         c.drawString(150, height, str(obj.genreFilm))
         height += 15
    c.save()
    return "OK"

def generate_film_pdf(db):
    c = Canvas("reports/film.pdf")
    pdfmetrics.registerFont(TTFont('FreeSans', 'FreeSans.ttf'))
    c.setFont(psfontname = 'FreeSans', size = 12)
    film_data = film_crud.get_film([], db)
    age_rating_data = age_rating_crud.get_age_raiting([], db)
    film_df = pd.DataFrame([o.__dict__ for o in film_data])
    age_rating_df = pd.DataFrame([o.__dict__ for o in age_rating_data])
    film_df = film_df.merge(age_rating_df, left_on='ageRaiting', right_on='ageRaiting')
    film_df = film_df[['idFilm','nameFilm','typeFilm','countryFilm','minAge','PGraiting','description_y','description_x']]
    height = 700
    c.drawString(250, 800,'Фильмы')
    for obj in film_df.iterrows():
         c.drawString(50, height, str(obj[1].idFilm))
         c.drawString(70, height, str(obj[1].nameFilm))
         c.drawString(150, height, str(obj[1].typeFilm))
         c.drawString(250, height, str(obj[1].countryFilm))
         c.drawString(300, height, str(obj[1].minAge))
         c.drawString(300, height+15, str(obj[1].PGraiting))
         c.drawString(350, height, str(obj[1].description_y))
         c.drawString(450, height, str(obj[1].description_x))
         height += 30
    c.save()
    return "OK"

def generate_ticket_pdf(db):
    c = Canvas("reports/ticket.pdf")
    pdfmetrics.registerFont(TTFont('FreeSans', 'FreeSans.ttf'))
    c.setFont(psfontname = 'FreeSans', size = 12)
    user_data = users_crud.get_client([], db)
    employee_data = employee_crud.get_employee([], db)
    ticket_data = ticket_crud.get_ticket([], db)
#     user_data = users_crud.get_client([], db)
    user_df = pd.DataFrame([o.__dict__ for o in user_data])
    employee_df = pd.DataFrame([o.__dict__ for o in employee_data])
    ticket_df = pd.DataFrame([o.__dict__ for o in ticket_data])
    ticket_df = ticket_df.merge(user_df, left_on='idClient', right_on='idClient')
    ticket_df = ticket_df[['idTransaction','idEmployee','ticketCost','startTime','Name','Surname','phoneNumber']]
    ticket_df = ticket_df.merge(employee_df, left_on='idEmployee', right_on='idEmployee')
    ticket_df = ticket_df[['idTransaction','ticketCost','startTime','Name_x','Surname_x','phoneNumber_x','Name_y','Surname_y','phoneNumber_y']]
   
    c.drawString(250, 800,'Билеты')
    height = 700
    c.drawString(50, height+40, 'ID')
    c.drawString(70, height+40, 'Цена')
    c.drawString(120, height+40, 'Дата продажи')
    c.drawString(300, height+40, 'Клиент')    
    c.drawString(400, height+40, 'Сотрудник')
    
    for obj in ticket_df.iterrows():
         c.drawString(50, height, str(obj[1].idTransaction))
         c.drawString(70, height, str(obj[1].ticketCost))
         c.drawString(120, height, str(obj[1].startTime))
         c.drawString(300, height, str(obj[1].Name_x))
         c.drawString(300, height-15, str(obj[1].Surname_x))
         c.drawString(300, height+15, str(obj[1].phoneNumber_x))
         c.drawString(400, height, str(obj[1].Name_y))
         c.drawString(400, height-15, str(obj[1].Surname_y))
         c.drawString(400, height+15, str(obj[1].phoneNumber_y))
         height -= 50
    c.save()
    return "OK"

def generate_genre_pdf(db):
#     c = Canvas("reports/ticket.pdf")
#     pdfmetrics.registerFont(TTFont('FreeSans', 'FreeSans.ttf'))
#     c.setFont(psfontname = 'FreeSans', size = 12)
#     film_data = film_crud.get_film([], db)
#     age_rating_data = age_rating_crud.get_age_raiting([], db)
#     ticket_df = pd.DataFrame([o.__dict__ for o in film_data])
#     age_rating_df = pd.DataFrame([o.__dict__ for o in age_rating_data])
#     ticket_df = ticket_df.merge(age_rating_df, left_on='ageRaiting', right_on='ageRaiting')
#     ticket_df = ticket_df[['idFilm','nameFilm','typeFilm','countryFilm','minAge','PGraiting','description_y','description_x']]
#     height = 700
#     c.drawString(250, 800,'Билеты')
#     for obj in ticket_df.iterrows():
#          c.drawString(50, height, str(obj[1].idFilm))
#          c.drawString(70, height, str(obj[1].nameFilm))
#          c.drawString(150, height, str(obj[1].typeFilm))
#          c.drawString(250, height, str(obj[1].countryFilm))
#          c.drawString(300, height, str(obj[1].minAge))
#          c.drawString(300, height+15, str(obj[1].PGraiting))
#          c.drawString(350, height, str(obj[1].description_y))
#          c.drawString(450, height, str(obj[1].description_x))
#          height += 30
#     c.save()
    return "OK"