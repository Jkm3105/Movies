from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.reservation import ReservationCreate
from services.reservation_service import ReservationService
from api.deps import get_db, get_current_user

router = APIRouter()
@router.post("/")
def reserve(
    payload: ReservationCreate,
    db: Session = Depends(get_db),
    user = Depends(get_current_user)
):
    print("USER DATA:", user)
    print("TYPE:", type(user))

    reservation = ReservationService().reserve(
        db=db,
        user_id=user["user_id"],
        showtime_id=payload.showtime_id,
        seat_ids=payload.seat_ids
    )

    return {
        "id": reservation.id,
        "user_id": reservation.user_id,
        "showtime_id": reservation.showtime_id,
        "status": reservation.status
    }
