from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.screen import ScreenCreate,ScreenResponse
from services.screen_service import ScreenService
from api.deps import get_db

router = APIRouter()

@router.post("/")
def create_screen(payload: ScreenCreate, db: Session = Depends(get_db)):
    return ScreenService().create_screen(db, payload)

@router.get("/", response_model=list[ScreenResponse])
def get_screen(db: Session = Depends(get_db)):
    return ScreenService().get_screen(db)

