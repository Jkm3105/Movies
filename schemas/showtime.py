from pydantic import BaseModel,Field
from datetime import datetime

class ShowtimeCreate(BaseModel):
    movie_id: str
    screen_id: str  
    start_time: datetime
    end_time: datetime
    total_seats: int = Field(..., gt=0)
    price: int

class ShowtimeResponse(BaseModel):
    start_time: datetime
    id: str
    total_seats: int
    movie_id: str
    screen_id: str
    end_time: datetime
    price: int
### Movie → Theatre → Screen → Showtime → Seats → Reservation