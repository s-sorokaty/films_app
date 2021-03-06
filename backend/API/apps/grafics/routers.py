from datetime import datetime
from fastapi import Depends, APIRouter, Response, HTTPException, Depends
from sqlalchemy.orm import Session
from starlette.responses import StreamingResponse
from apps.repository import SessionLocal, engine

from apps.grafics import crud


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/')
async def get_place_info(min_date:datetime, max_date:datetime, db: Session = Depends(get_db)):
    crud.get_place_info(db)
    crud.get_ticket_info(db, min_date, max_date)
    crud.get_employee_info(db)
    crud.get_client_info(db)
    crud.get_film_info(db)
    return 'OK'