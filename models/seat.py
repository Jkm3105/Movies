from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from core.database import Base
import uuid

class Seat(Base):
    __tablename__ = "seats"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    seat_number = Column(String, nullable=False)  # e.g. A1, B5
    row = Column(String, nullable=False)
    price = Column(Integer, nullable=False)

    screen_id = Column(String, ForeignKey("screens.id"))

    # Relationship
    screen = relationship("Screen", back_populates="seats")