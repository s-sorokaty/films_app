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


@router.post('/info', status_code=200)
async def add_film(film: shemas.film, db: Session = Depends(get_db)):
    try:
        crud.add_film(film, db)
        return "OK"
    except:
        raise HTTPException(status_code=500, detail="Server Error")


@router.delete('/info')
async def delete_film(film: shemas.film, db: Session = Depends(get_db)):
    try:
        crud.delete_film(film, db)
        return "OK"
    except:
        raise HTTPException(status_code=500, detail="Server Error")


@router.put('/info')
async def update_film(film: shemas.film, db: Session = Depends(get_db)):
    try:
        crud.update_film(film, db)
        return "OK"
    except:
        raise HTTPException(status_code=500, detail="Server Error")


@router.get('/info')
async def get_film(film: shemas.film = None, db: Session = Depends(get_db)):
    try:
        return crud.get_film(film, db)
    except KeyError:
        print(KeyError)
        raise HTTPException(status_code=500, detail="Server Error")




@router.post('/genre', status_code=200)
async def add_genre(film: shemas.genre_on_film, db: Session = Depends(get_db)):
    try:
        crud.add_genre(film, db)
        return "OK"
    except:
        raise HTTPException(status_code=500, detail="Server Error")


@router.delete('/genre')
async def delete_genre(film: shemas.genre_on_film, db: Session = Depends(get_db)):
    try:
        crud.delete_genre(film, db)
        return "OK"
    except:
        raise HTTPException(status_code=500, detail="Server Error")


@router.put('/genre')
async def update_film(film: shemas.genre_on_film, db: Session = Depends(get_db)):
    try:
        crud.update_genre(film, db)
        return "OK"
    except:
        raise HTTPException(status_code=500, detail="Server Error")


@router.get('/genre')
async def get_film(film: shemas.genre_on_film = None, db: Session = Depends(get_db)):
    try:
        return crud.get_genre(film, db)
    except:
        raise HTTPException(status_code=500, detail="Server Error")

@router.get('/info/coloums')
async def get_coloums(db: Session = Depends(get_db)):
    try:
        return crud.get_film_columns_descriptions(db)
    except:
        raise HTTPException(status_code=500, detail="Server Error")

@router.get('/genre/coloums')
async def get_coloums(db: Session = Depends(get_db)):
    try:
        return crud.get_genre_columns_descriptions(db)
    except:
        raise HTTPException(status_code=500, detail="Server Error")
