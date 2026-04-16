from sqlalchemy import Column, String, UniqueConstraint
from core.database import Base

class ReservationSeat(Base):
    __tablename__ = "reservation_seats"

    id = Column(String, primary_key=True)
    reservation_id = Column(String)
    showtime_id = Column(String)
    seat_id = Column(String)

    __table_args__ = (
        UniqueConstraint("showtime_id", "seat_id", name="unique_seat_booking"),
    ) 