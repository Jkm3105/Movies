from sqlalchemy import Column, String, DateTime, ForeignKey
from core.database import Base
import uuid
from datetime import datetime

class Reservation(Base):
    __tablename__ = "reservations"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("users.id"))
    showtime_id = Column(String, ForeignKey("showtimes.id"))
    status = Column(String, default="CONFIRMED")
    created_at = Column(DateTime, default=datetime.utcnow)