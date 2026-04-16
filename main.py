from fastapi import FastAPI
from api.router import api_router
from core.database import Base, engine

# IMPORT ALL MODELS HERE 👇
from models.user import User
from models.movie import Movie
from models.showtime import Showtime
from models.screen import Screen
from models.theatre import Theatre
from models.seat import Seat
from models.reservation import Reservation
from models.genre import Genre  # if exists

app = FastAPI(title="Movie Reservation API")

Base.metadata.create_all(bind=engine)

app.include_router(api_router)