from pydantic import BaseModel

class SeatCreate(BaseModel):
    seat_number: str
    row: str
    price: int
    screen_id: str


class SeatResponse(BaseModel):
    id: str
    seat_number: str
    row: str
    price: int
    screen_id: str

    class Config:
        from_attributes = True