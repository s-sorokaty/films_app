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
    print(db_employeer)
    if type(db_employeer) == models.employee_info:
        db.delete(db_employeer)
        db.commit()
        return True
    else:
        raise False
