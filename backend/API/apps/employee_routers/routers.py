from fastapi import Depends, APIRouter, Response, status
from sqlalchemy.orm import Session
from apps.repository import SessionLocal, engine

from apps.employee_routers import crud, shemas
router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/')
async def add_employee(employeer: shemas.employeer, db: Session = Depends(get_db)):
    crud.add_employee(employeer, db)
    return "ok"


@router.delete('/')
async def delete_employee(employeer: shemas.employeer, db: Session = Depends(get_db)):
    crud.delete_employee(employeer, db)
    return "ok"
