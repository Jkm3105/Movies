from sqlalchemy import Column, String, Text
from core.database import Base
import uuid

class Movie(Base):
    __tablename__ = "movies"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String, nullable=False)
    description = Column(Text)
    poster_url = Column(String)
    genre = Column(String)