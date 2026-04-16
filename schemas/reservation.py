from pydantic import BaseModel
from typing import List

class ReservationCreate(BaseModel):
    user_id: str
    showtime_id: str
    seat_ids: List[str]


class ReservationResponse(BaseModel):
    id: str
    user_id: str
    showtime_id: str

    class Config:
        from_attributes = True