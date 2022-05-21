from fastapi import Depends, APIRouter, Response, HTTPException
from sqlalchemy.orm import Session
from apps.repository import SessionLocal, engine

from apps.age_rating_routers import crud, shemas


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/', status_code=200)
async def add_age_raiting(age_raiting: shemas.age_rating_type, db: Session = Depends(get_db)):
    try:
        crud.add_age_raiting(age_raiting, db)
        return "OK"
    except:
        raise HTTPException(status_code=500, detail="Server Error")


@router.delete('/')
async def delete_age_raiting(age_raiting: shemas.age_rating_type, db: Session = Depends(get_db)):
    try:
        crud.delete_age_raiting(age_raiting, db)
        return "OK"
    except:
        raise HTTPException(status_code=500, detail="Server Error")


@router.put('/')
async def update_age_raiting(age_raiting: shemas.age_rating_type, db: Session = Depends(get_db)):
    try:
        crud.update_age_raiting(age_raiting, db)
        return "OK"
    except:
        raise HTTPException(status_code=500, detail="Server Error")


@router.get('/')
async def get_age_raiting(age_raiting: shemas.age_rating_type = None, db: Session = Depends(get_db)):
    try:
        return crud.get_age_raiting(age_raiting, db)
    except:
        raise HTTPException(status_code=500, detail="Server Error")
