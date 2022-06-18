from fastapi import Depends, APIRouter, Response, HTTPException, Depends
from sqlalchemy.orm import Session
from starlette.responses import StreamingResponse
from apps.repository import SessionLocal, engine

from apps.reports import crud


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/')
async def get_place_info(db: Session = Depends(get_db)):
    crud.generate_users_pdf(db)
    crud.generate_employee_pdf(db)
    crud.generate_genre_pdf(db)
    crud.generate_film_pdf(db)
    crud.generate_ticket_pdf(db)
    crud.generate_session_pdf(db)
    return "OK"

