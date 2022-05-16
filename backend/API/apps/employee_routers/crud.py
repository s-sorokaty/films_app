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
    db.query(models.employee_info).filter(
        models.employee_info.idEmployee == employeer.idEmployee)\
        .update({'idEmployee': db_employeer.idEmployee,
                 'Name': db_employeer.Name,
                 'Surname': db_employeer.Surname,
                 'phoneNumber': db_employeer.phoneNumber
                 })
    db.commit()


def get_employee(employeer, min, max, db):
    if employeer:
        return db.query(models.employee_info).filter(
            models.employee_info.idEmployee == employeer.idEmployee).first()
    else:
        return db.query(models.employee_info).filter(
            models.employee_info.idEmployee >= min, models.employee_info.idEmployee <= max).limit(5).all()
