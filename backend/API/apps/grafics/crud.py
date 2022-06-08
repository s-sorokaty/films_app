from sqlalchemy.orm import Session
from datetime import datetime
from apps.place_routers.models import place_info 
from apps.ticket_info_routers.models import ticket_info
import matplotlib.pyplot as plt
import pandas as pd

def get_place_info(db):
    place_data = db.query(place_info).all()
    place_df = pd.DataFrame([o.__dict__ for o in place_data])
    place_df.loc[(place_df['placeType'] == 'базовое'), 'placeType'] = 0
    place_df.loc[(place_df['placeType'] == 'премиум'), 'placeType'] = 1
    fig, ax = plt.subplots()
    ax.set_title('Расределение мест по залам') 
    ax.set_xlabel('ID зала')
    ax.set_ylabel('Качество места (Больше - лучше)')
    ax.scatter(x = place_df['idHall'], y = place_df['placeType'])
    ax.legend()
    fig.savefig('graphics/hall_info')
    return 'OK'

def get_ticket_info(db, min_date, max_date):
    ticket_data = db.query(ticket_info).all()
    ticket_df = pd.DataFrame([o.__dict__ for o in ticket_data])
    ticket_df = ticket_df[(ticket_df['startTime'] >= min_date) & (ticket_df['startTime'] <= max_date)]
    print(ticket_df)
    fig, ax = plt.subplots()
    ax.set_title('Продажи билетов') 
    ax.set_xlabel('цены за билет')
    ax.set_ylabel('дата продажи')
    ax.scatter(x = ticket_df['startTime'], y = ticket_df['ticketCost'])
    ax.legend()
    fig.savefig('graphics/ticket_info')
    return 'OK'

def get_employee_info(db):
    ticket_data = db.query(ticket_info).all()
    ticket_df = pd.DataFrame([o.__dict__ for o in ticket_data])
    count = ticket_df['idEmployee'].value_counts()
    fig, ax = plt.subplots()
    ax.set_title('Продажи билетов') 
    ax.set_xlabel('ID сотруднка')
    ax.set_ylabel('кол-во продаж')
    ax.scatter(x = count.keys(), y = count.values)
    ax.legend()
    fig.savefig('graphics/employee_info')
    return 'OK'

def get_client_info(db):
    ticket_data = db.query(ticket_info).all()
    ticket_df = pd.DataFrame([o.__dict__ for o in ticket_data])
    count = ticket_df['idClient'].value_counts()
    print(count.values)
    print(count.keys()) 
    fig, ax = plt.subplots()
    ax.set_title('Продажи билетов') 
    ax.set_xlabel('ID клиента')
    ax.set_ylabel('кол-во посещений')
    ax.scatter(x = count.keys(), y = count.values)
    ax.legend()
    fig.savefig('graphics/client_info')
    return 'OK'