from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from core.database import Base
import uuid

class Theatre(Base):
    __tablename__ = "theatres"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)

    screens = relationship("Screen", back_populates="theatre", cascade="all, delete")