from fastapi import Depends, APIRouter, Response, HTTPException
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


@router.post('/', status_code=200)
async def add_employee(employeer: shemas.employeer, db: Session = Depends(get_db)):
    try:
        crud.add_employee(employeer, db)
        return "OK"
    except:
        raise HTTPException(status_code=500, detail="Server Error")


@router.delete('/')
async def delete_employee(employeer: shemas.employeer, db: Session = Depends(get_db)):
    try:
        crud.delete_employee(employeer, db)
        return "OK"
    except:
        raise HTTPException(status_code=500, detail="Server Error")


@router.put('/')
async def update_employee(employeer: shemas.employeer, db: Session = Depends(get_db)):
    try:
        crud.update_employee(employeer, db)
        return "OK"
    except:
        raise HTTPException(status_code=500, detail="Server Error")


@router.get('/')
async def get_employee(employeer: shemas.employeer = Depends(), db: Session = Depends(get_db)):
    try:
        return crud.get_employee(employeer, db)
    except:
        raise HTTPException(status_code=500, detail="Server Error")

@router.get('/coloums')
async def get_coloums(db: Session = Depends(get_db)):
    try:
        return crud.get_columns_descriptions(db)
    except:
        raise HTTPException(status_code=500, detail="Server Error")
