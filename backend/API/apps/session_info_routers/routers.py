from fastapi import Depends, APIRouter, Response, HTTPException, Depends
from sqlalchemy.orm import Session
from apps.repository import SessionLocal, engine

from apps.session_info_routers import crud, shemas


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/session', status_code=200)
async def add_session(session_info: shemas.session_info, db: Session = Depends(get_db)):
    try:
        crud.add_session_info(session_info, db)
        return "OK"
    except KeyError:
        print(KeyError)
        raise HTTPException(status_code=500, detail="Server Error")


@router.delete('/session')
async def delete_session_info(session_info: shemas.session_info, db: Session = Depends(get_db)):
    try:
        crud.delete_session_info(session_info, db)
        return "OK"
    except:
        raise HTTPException(status_code=500, detail="Server Error")


@router.put('/session')
async def update_session_info(session_info: shemas.session_info, db: Session = Depends(get_db)):
    try:
        crud.update_session_info(session_info, db)
        return "OK"
    except:
        raise HTTPException(status_code=500, detail="Server Error")


@router.get('/session')
async def get_session_info(session_info: shemas.session_info = Depends(), db: Session = Depends(get_db)):
    try:
        return crud.get_session_info(session_info, db)
    except:
        raise HTTPException(status_code=500, detail="Server Error")

@router.get('/session/coloums')
async def get_coloums(db: Session = Depends(get_db)):
    try:
        return crud.get_columns_descriptions_session_info(db)
    except:
        raise HTTPException(status_code=500, detail="Server Error")


@router.post('/session-film', status_code=200)
async def add_film_on_session(film_on_session: shemas.film_on_session, db: Session = Depends(get_db)):
    try:
        crud.add_film_on_session(film_on_session, db)
        return "OK"
    except KeyError:
        print(KeyError)
        raise HTTPException(status_code=500, detail="Server Error")


@router.delete('/session-film')
async def delete_film_on_session(film_on_session: shemas.film_on_session, db: Session = Depends(get_db)):
    try:
        crud.delete_film_on_session(film_on_session, db)
        return "OK"
    except:
        raise HTTPException(status_code=500, detail="Server Error")


@router.put('/session-film')
async def update_film_on_session(film_on_session: shemas.film_on_session, db: Session = Depends(get_db)):
    try:
        crud.update_film_on_session(film_on_session, db)
        return "OK"
    except:
        raise HTTPException(status_code=500, detail="Server Error")


@router.get('/session-film')
async def get_film_on_session(film_on_session: shemas.film_on_session = Depends(), db: Session = Depends(get_db)):
    try:
        return crud.get_film_on_session(film_on_session, db)
    except:
        raise HTTPException(status_code=500, detail="Server Error")

@router.get('/session-film/coloums')
async def get_coloums(db: Session = Depends(get_db)):
    try:
        return crud.get_columns_descriptions_film_on_session(db)
    except:
        raise HTTPException(status_code=500, detail="Server Error")
