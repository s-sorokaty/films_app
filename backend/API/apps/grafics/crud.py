import pandas as pd
import matplotlib.pyplot as plt
from apps.place_routers.models import place_info
from apps.ticket_info_routers.models import ticket_info
from apps.client_routers.models import client_info
from apps.session_info_routers.models import session_info, film_on_session
from apps.film_info_routers.models import film_info
from apps.employee_routers.models import employee_info


def get_place_info(db):
    place_data = db.query(place_info).all()
    place_df = pd.DataFrame([o.__dict__ for o in place_data])
    place_df.loc[(place_df['placeType'] == 'базовое'), 'placeType'] = 0
    place_df.loc[(place_df['placeType'] == 'премиум'), 'placeType'] = 1
    fig, ax = plt.subplots()
    ax.set_title('Расределение мест по залам')
    ax.set_xlabel('ID зала')
    ax.set_ylabel('Качество места (Больше - лучше)')
    ax.scatter(x=place_df['idHall'], y=place_df['placeType'])
    ax.xaxis.get_children()[1].set_size(1000)
    ax.legend()
    fig.savefig('graphics/hall_info')
    return 'OK'


def get_ticket_info(db, min_date, max_date):
    ticket_data = db.query(ticket_info).all()
    ticket_df = pd.DataFrame([o.__dict__ for o in ticket_data])
    ticket_df = ticket_df[(ticket_df['startTime'] >= min_date) & (
        ticket_df['startTime'] <= max_date)]
    fig, ax = plt.subplots()
    ax.set_title('Продажи билетов')
    ax.set_xlabel('цены за билет')
    ax.set_ylabel('дата продажи')
    ax.scatter(x=ticket_df['startTime'], y=ticket_df['ticketCost'], alpha =0.1)
    ax.xaxis.get_children()[1].set_size(1000)
    ax.legend()
    fig.savefig('graphics/ticket_info')
    return 'OK'


def get_employee_info(db):
    ticket_data = db.query(ticket_info).all()
    ticket_df = pd.DataFrame([o.__dict__ for o in ticket_data])
    employee_data = db.query(employee_info).all()
    employee_df = pd.DataFrame([o.__dict__ for o in employee_data])

    ticket_df = ticket_df.merge(
        employee_df, left_on='idEmployee', right_on='idEmployee')
    ticket_df['All_name'] = ticket_df['Name'] + '\n' + ticket_df['Surname']
    count = ticket_df['idEmployee'].value_counts()
    fig, ax = plt.subplots()
    print(ticket_df['All_name'])
    print(count)
    ax.set_title('Продажи билетов')
    ax.set_xlabel('ID сотруднка')
    ax.set_ylabel('кол-во продаж')
    ax.bar(pd.unique(ticket_df['All_name']), count.values, width=0.1)
    ax.xaxis.get_children()[1].set_size(1000)
    ax.legend()
    fig.savefig('graphics/employee_info')
    return 'OK'


def get_client_info(db):
    ticket_data = db.query(ticket_info).all()
    client_data = db.query(client_info).all()
    ticket_df = pd.DataFrame([o.__dict__ for o in ticket_data])
    client_df = pd.DataFrame([o.__dict__ for o in client_data])
    ticket_df = ticket_df.merge(
        client_df, left_on='idClient', right_on='idClient')
    
    ticket_df['All_name'] = ticket_df['Name'] + '\n' + ticket_df['Surname']
    count = ticket_df['idClient'].value_counts()
    fig, ax = plt.subplots()
    ax.bar(pd.unique(ticket_df['All_name']), count.values, width=0.1)
    ax.set_title('Продажи билетов')
    ax.set_xlabel('ID клиента')
    ax.set_ylabel('кол-во посещений')
    # ax.set_xlim(0,20)
    ax.legend()
    fig.savefig('graphics/client_info')
    return 'OK'

def get_film_info(db):
    ticket_data = db.query(ticket_info).all()
    ticket_df = pd.DataFrame([o.__dict__ for o in ticket_data])
    session_data = db.query(session_info).all()
    film_data = db.query(film_info).all() 
    session_df = pd.DataFrame([o.__dict__ for o in session_data])
    
    ticket_df = ticket_df.merge(
        session_df, left_on='idSession', right_on='idSession')
    
    film_on_session_data = db.query(film_on_session).all()
    film_on_session_df = pd.DataFrame([o.__dict__ for o in film_on_session_data])
    # print(film_on_session_df)
    ticket_df = ticket_df.merge(
        film_on_session_df, left_on='idSession', right_on='idSession')
    film_df = pd.DataFrame([o.__dict__ for o in film_data])
    print(ticket_df[['idTransaction','idFilm']])
    ticket_df = ticket_df.merge(
        film_df, left_on='idFilm', right_on='idFilm')
    fig, ax = plt.subplots()
    ax.set_title('Продажи билетов')
    ax.set_xlabel('название фильма')
    ax.set_ylabel('кол-во продаж')
    ax.bar(ticket_df['nameFilm'], ticket_df['idTransaction'], width=0.1)
    ax.legend()
    fig.savefig('graphics/films_tickets_info')
    return 'OK'