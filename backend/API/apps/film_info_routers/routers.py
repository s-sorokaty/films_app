from fastapi import Depends, APIRouter, Response, HTTPException
from sqlalchemy.orm import Session
from apps.repository import SessionLocal, engine

from apps.film_info_routers import crud, shemas


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/', status_code=200)
async def add_film(film: shemas.film, db: Session = Depends(get_db)):
    try:
        crud.add_film(film, db)
        return "OK"
    except:
        raise HTTPException(status_code=500, detail="Server Error")


@router.delete('/')
async def delete_film(film: shemas.film, db: Session = Depends(get_db)):
    try:
        crud.delete_film(film, db)
        return "OK"
    except:
        raise HTTPException(status_code=500, detail="Server Error")


@router.put('/')
async def update_film(film: shemas.film, db: Session = Depends(get_db)):
    try:
        crud.update_film(film, db)
        return "OK"
    except:
        raise HTTPException(status_code=500, detail="Server Error")


@router.get('/')
async def get_film(film: shemas.film = None, db: Session = Depends(get_db)):
    try:
        return crud.get_film(film, db)
    except:
        raise HTTPException(status_code=500, detail="Server Error")
