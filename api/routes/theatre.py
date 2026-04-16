from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.theatre import TheatreCreate,TheatreResponse
from services.theatre_service import TheatreService
from api.deps import get_db

router = APIRouter()

@router.post("/")
def create_theatre(payload: TheatreCreate, db: Session = Depends(get_db)):
    return TheatreService().create_theatre(db, payload)

@router.get("/", response_model=list[TheatreResponse])
def get_theatre(db: Session = Depends(get_db)):
    return TheatreService().get_theatre(db)

