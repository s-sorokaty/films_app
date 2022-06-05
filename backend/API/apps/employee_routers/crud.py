from sqlalchemy.orm import Session
from apps.employee_routers import shemas, models


def create_db_emploeer(employeer):
    return models.employee_info(
        idEmployee=employeer.idEmployee,
        Name=employeer.Name,
        Surname=employeer.Surname,
        phoneNumber=employeer.phoneNumber,
    )


def add_employee(employeer, db):
    db_employeer = create_db_emploeer(employeer)
    db.add(db_employeer)
    db.commit()
    db.refresh(db_employeer)


def delete_employee(employeer, db):
    db_employeer = db.query(models.employee_info).filter(
        models.employee_info.idEmployee == employeer.idEmployee).first()
    if type(db_employeer) == models.employee_info:
        db.delete(db_employeer)
        db.commit()
        return True
    else:
        raise False


def update_employee(employeer, db):
    db_employeer = create_db_emploeer(employeer)
    res = db.query(models.employee_info).filter(
        models.employee_info.idEmployee == employeer.idEmployee)
    if res.first() == None:
        raise
    res.update({'idEmployee': db_employeer.idEmployee,
                'Name': db_employeer.Name,
                'Surname': db_employeer.Surname,
                'phoneNumber': db_employeer.phoneNumber
                })
    db.commit()


def get_employee(employee, db):
    query_db =  db.query(models.employee_info)
    for key in employee:
        if key[1]:
            print(getattr(models.employee_info, key[0]), key[1])
            query_db = query_db.filter(
                getattr(models.employee_info, key[0]) == key[1]
            )
    return query_db.all() 
            

def get_columns_descriptions(db):
    return db.query(models.employee_info).statement.columns.keys()
