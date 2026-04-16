
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.deps import get_db
from schemas.seat import SeatCreate, SeatResponse
from services.seat_service import SeatService

router = APIRouter()

@router.post("/", response_model=SeatResponse)
def create_seat(payload: SeatCreate, db: Session = Depends(get_db)):
    return SeatService().create_seat(db, payload)


@router.get("/", response_model=list[SeatResponse])
def get_seats(db: Session = Depends(get_db)):
    return SeatService().get_seats(db)


@router.get("/screen/{screen_id}", response_model=list[SeatResponse])
def get_seats_by_screen(screen_id: str, db: Session = Depends(get_db)):
    return SeatService().get_seats_by_screen(db, screen_id)