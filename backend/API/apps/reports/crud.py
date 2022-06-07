from sqlalchemy.orm import Session
from apps.client_routers import crud as users_crud
from apps.employee_routers import crud as employee_crud
from apps.film_genre_routers import crud as genre_crud
from apps.place_routers.models import place_info
from apps.ticket_info_routers.models import ticket_info
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def generate_users_pdf(db):
    c = Canvas("reports/users.pdf")
    users = users_crud.get_client([], db)
    pdfmetrics.registerFont(TTFont('FreeSans', 'FreeSans.ttf'))
    c.setFont(psfontname = 'FreeSans', size = 14)
    c.drawCentredString(250, 800,'Клиенты')
    height = 700
    for obj in users:
         c.drawString(100, height, str(obj.idClient))
         c.drawString(150, height, str(obj.Name))
         c.drawString(300, height, str(obj.Surname))
         c.drawString(500, height, str(obj.phoneNumber))
         height += 15
    c.save()
    return 'OK'


def generate_employee_pdf(db):
    c = Canvas("reports/employee.pdf")
    employee = employee_crud.get_employee([], db)
    pdfmetrics.registerFont(TTFont('FreeSans', 'FreeSans.ttf'))
    c.setFont(psfontname = 'FreeSans', size = 14)
    height = 700
    c.drawString(250, 800,'Сотрудники')
    for obj in employee:
         c.drawString(100, height, str(obj.idEmployee))
         c.drawString(150, height, str(obj.Name))
         c.drawString(300, height, str(obj.Surname))
         c.drawString(500, height, str(obj.phoneNumber))
         height += 15
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