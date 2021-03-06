from fastapi import Depends, APIRouter, Response, HTTPException
from sqlalchemy.orm import Session
from apps.repository import SessionLocal, engine

from apps.film_genre_routers import crud, shemas


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/', status_code=200)
async def add_genre(genre: shemas.genre, db: Session = Depends(get_db)):
    try:
        crud.add_genre(genre, db)
        return "OK"
    except:
        raise HTTPException(status_code=500, detail="Server Error")


@router.delete('/')
async def delete_genre(genre: shemas.genre, db: Session = Depends(get_db)):
    try:
        crud.delete_genre(genre, db)
        return "OK"
    except:
        raise HTTPException(status_code=500, detail="Server Error")


@router.put('/')
async def update_genre(genre: shemas.genre, db: Session = Depends(get_db)):
    try:
        crud.update_genre(genre, db)
        return "OK"
    except:
        raise HTTPException(status_code=500, detail="Server Error")


@router.get('/')
async def get_genre(genre: shemas.genre = Depends(), db: Session = Depends(get_db)):
    try:
        return crud.get_genre(genre, db)
    except:
        raise HTTPException(status_code=500, detail="Server Error")

@router.get('/coloums')
async def get_coloums(db: Session = Depends(get_db)):
    try:
        return crud.get_columns_descriptions(db)
    except:
        raise HTTPException(status_code=500, detail="Server Error")
