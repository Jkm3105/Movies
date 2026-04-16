from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.showtime import ShowtimeCreate,ShowtimeResponse
from services.showtime_service import ShowtimeService
from api.deps import get_db

router = APIRouter()

@router.post("/")
def create_showtime(payload: ShowtimeCreate, db: Session = Depends(get_db)):
    service = ShowtimeService()
    return service.create_showtime(db, payload)

@router.get("/", response_model=list[ShowtimeResponse])
def get_showtime(db: Session = Depends(get_db)):
    return ShowtimeService().get_showtime(db)