from fastapi import Depends, APIRouter, Response, HTTPException
from sqlalchemy.orm import Session
from apps.repository import SessionLocal, engine

from apps.ticket_info_routers import crud, shemas


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/', status_code=200)
async def add_ticket(ticket: shemas.ticket, db: Session = Depends(get_db)):
    try:
        crud.add_ticket(ticket, db)
        return "OK"
    except:
        raise HTTPException(status_code=500, detail="Server Error")


@router.delete('/')
async def delete_ticket(ticket: shemas.ticket, db: Session = Depends(get_db)):
    try:
        crud.delete_ticket(ticket, db)
        return "OK"
    except:
        raise HTTPException(status_code=500, detail="Server Error")


@router.put('/')
async def update_ticket(ticket: shemas.ticket, db: Session = Depends(get_db)):
    try:
        crud.update_ticket(ticket, db)
        return "OK"
    except:
        raise HTTPException(status_code=500, detail="Server Error")


@router.get('/')
async def get_ticket(ticket: shemas.ticket = None, db: Session = Depends(get_db)):
    try:
        return crud.get_ticket(ticket, db)
    except KeyError:
        print(KeyError)
        raise HTTPException(status_code=500, detail="Server Error")

@router.get('/coloums')
async def get_coloums(db: Session = Depends(get_db)):
    try:
        return crud.get_columns_descriptions(db)
    except:
        raise HTTPException(status_code=500, detail="Server Error")
