from sqlalchemy.orm import Session
from apps.ticket_info_routers import shemas, models


def create_db_ticket(ticket):
    return models.ticket_info(
        idTransaction=ticket.idTransaction,
        idSession=ticket.idSession,
        idEmployee=ticket.idEmployee,
        idHall=ticket.idHall,
        ticketCost=ticket.ticketCost,
        startTime=ticket.startTime,
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
                 'idHall': db_ticket.idHall,
                 'ticketCost': db_ticket.ticketCost,
                 'startTime': db_ticket.startTime
                 })
    db.commit()


def get_ticket(ticket, db):
    if ticket:
        return db.query(models.ticket_info).filter(
            models.ticket_info.idTransaction == ticket.idTransaction).first()
    else:
        return db.query(models.ticket_info).limit(500).all()
        
def get_columns_descriptions(db):
    return db.query(models.place_info).statement.columns.keys()
