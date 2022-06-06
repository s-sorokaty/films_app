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
async def get(db: Session = Depends(get_db)):
    # try:
    return crud.get(db)
    # except:
    #     raise HTTPException(status_code=500, detail="Server Error")