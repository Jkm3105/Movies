from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from core.database import Base
import uuid

class Showtime(Base):
    __tablename__ = "showtimes"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    movie_id = Column(String, ForeignKey("movies.id"))
    screen_id = Column(String, ForeignKey("screens.id"))
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    total_seats = Column(Integer, nullable=False)
    price = Column(Integer,nullable=False)
    