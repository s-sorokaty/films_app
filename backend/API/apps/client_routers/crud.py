from sqlalchemy.orm import Session
from apps.client_routers import shemas, models


def create_db_client(client):
    return models.client_info(
        idClient=client.idClient,
        Name=client.Name,
        Surname=client.Surname,
        phoneNumber=client.phoneNumber,
    )


def add_client(client, db):
    db_client = create_db_client(client)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)


def delete_client(client, db):
    db_client = db.query(models.client_info).filter(
        models.client_info.idClient == client.idClient).first()
    if type(db_client) == models.client_info:
        db.delete(db_client)
        db.commit()
        return True
    else:
        raise False


def update_client(client, db):
    db_client = create_db_client(client)
    db.query(models.client_info).filter(
        models.client_info.idClient == client.idClient)\
        .update({'idClient': db_client.idClient,
                 'Name': db_client.Name,
                 'Surname': db_client.Surname,
                 'phoneNumber': db_client.phoneNumber
                 })
    db.commit()


def get_client(client, db):
    query_db =  db.query(models.client_info)
    for key in client:
        if key[1]:
            print(getattr(models.client_info, key[0]), key[1])
            query_db = query_db.filter(
                getattr(models.client_info, key[0]) == key[1]
            )
    return query_db.all() 


def get_columns_descriptions(db):
    return db.query(models.client_info).statement.columns.keys()
