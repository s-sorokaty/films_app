from fastapi import Depends, APIRouter, Response, HTTPException
from sqlalchemy.orm import Session
from apps.repository import SessionLocal, engine

from apps.client_routers import crud, shemas


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/', status_code=200)
async def add_client(client: shemas.client, db: Session = Depends(get_db)):
    try:
        crud.add_client(client, db)
        return "OK"
    except:
        raise HTTPException(status_code=500, detail="Server Error")


@router.delete('/')
async def delete_client(client: shemas.client, db: Session = Depends(get_db)):
    try:
        crud.delete_client(client, db)
        return "OK"
    except:
        raise HTTPException(status_code=500, detail="Server Error")


@router.put('/')
async def update_client(client: shemas.client, db: Session = Depends(get_db)):
    try:
        crud.update_client(client, db)
        return "OK"
    except:
        raise HTTPException(status_code=500, detail="Server Error")


@router.get('/')
async def get_client(client: shemas.client = Depends(), db: Session = Depends(get_db)):
    try:
        return crud.get_client(client, db)
    except:
        raise HTTPException(status_code=500, detail="Server Error")

@router.get('/coloums')
async def get_coloums(db: Session = Depends(get_db)):
    try:
        return crud.get_columns_descriptions(db)
    except:
        raise HTTPException(status_code=500, detail="Server Error")
