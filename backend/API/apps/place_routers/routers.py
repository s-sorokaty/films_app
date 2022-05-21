from fastapi import Depends, APIRouter, Response, HTTPException
from sqlalchemy.orm import Session
from apps.repository import SessionLocal, engine

from apps.place_routers import crud, shemas


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/', status_code=200)
async def add_place(place: shemas.place, db: Session = Depends(get_db)):
    try:
        crud.add_place(place, db)
        return "OK"
    except KeyError:
        print(KeyError)
        raise HTTPException(status_code=500, detail="Server Error")


@router.delete('/')
async def delete_place(place: shemas.place, db: Session = Depends(get_db)):
    try:
        crud.delete_place(place, db)
        return "OK"
    except:
        raise HTTPException(status_code=500, detail="Server Error")


@router.put('/')
async def update_place(place: shemas.place, db: Session = Depends(get_db)):
    try:
        crud.update_place(place, db)
        return "OK"
    except:
        raise HTTPException(status_code=500, detail="Server Error")


@router.get('/')
async def get_place(place: shemas.place = None, db: Session = Depends(get_db)):
    try:
        return crud.get_place(place, db)
    except:
        raise HTTPException(status_code=500, detail="Server Error")
