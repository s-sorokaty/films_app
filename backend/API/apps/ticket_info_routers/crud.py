from sqlalchemy.orm import Session
from apps.ticket_info_routers import shemas, models
from datetime import datetime

def create_db_ticket(ticket):
    return models.ticket_info(
        idTransaction=ticket.idTransaction,
        idSession=ticket.idSession,
        idEmployee=ticket.idEmployee,
        idClient=ticket.idClient,
        idHall=ticket.idHall,
        idPlace=ticket.idPlace,
        ticketCost=ticket.ticketCost,
        startTime=datetime.fromtimestamp(ticket.startTime),
    )


def add_ticket(ticket, db):
    db_ticket = create_db_ticket(ticket)
    db.add(db_ticket)
    db.commit()
    db.refresh(db_ticket)


def delete_ticket(ticket, db):
    db_ticket = db.query(models.ticket_info).filter(
        models.ticket_info.idTransaction == ticket.idTransaction).first()
    if type(db_ticket) == models.ticket_info:
        db.delete(db_ticket)
        db.commit()
        return "OK"
    else:
        raise None


def update_ticket(ticket, db):
    db_ticket = create_db_ticket(ticket)
    db.query(models.ticket_info).filter(
        models.ticket_info.idTransaction == ticket.idTransaction)\
        .update({'idTransaction': db_ticket.idTransaction,
                 'idSession': db_ticket.idSession,
                 'idEmployee': db_ticket.idEmployee,
                 'idClient': db_ticket.idClient,
                 'idHall': db_ticket.idHall,
                 'idPlace': db_ticket.idPlace,
                 'ticketCost': db_ticket.ticketCost,
                 'startTime': db_ticket.startTime
                 })
    db.commit()


def get_ticket(ticket, db):
    query_db =  db.query(models.ticket_info)
    for key in ticket:
        if key[1]:
            print(getattr(models.ticket_info, key[0]), key[1])
            query_db = query_db.filter(
                getattr(models.ticket_info, key[0]) == key[1]
            )
    return query_db.all() 
        
def get_columns_descriptions(db):
    return db.query(models.ticket_info).statement.columns.keys()
