from sqlalchemy import create_engine
print("SQLAlchemy working")
from sqlalchemy.orm import sessionmaker,declarative_base
from core.config import settings
engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()