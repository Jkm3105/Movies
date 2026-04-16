from fastapi import APIRouter
from api.routes import auth, movies, showtimes, reservations, theatre, screen, seat, reservations

api_router = APIRouter()

api_router.include_router(auth.router, prefix="/auth")
api_router.include_router(movies.router, prefix="/movies")
api_router.include_router(showtimes.router, prefix="/showtimes")
api_router.include_router(reservations.router, prefix="/reservations")
api_router.include_router(theatre.router,prefix="/theatre")
api_router.include_router(screen.router,prefix="/screen")
api_router.include_router(seat.router,prefix="/seat")
api_router.include_router(reservations.router,prefix="/reservations")





