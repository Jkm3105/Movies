from sqlalchemy import Column, String
from core.database import Base
import uuid

class Genre(Base):
    __tablename__ = "genres"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, unique=True, nullable=False)