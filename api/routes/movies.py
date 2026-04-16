from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.movie import MovieCreate, MovieResponse
from services.movie_service import MovieService
from api.deps import get_db

router = APIRouter()

@router.post("/", response_model=MovieResponse)
def create_movie(payload: MovieCreate, db: Session = Depends(get_db)):
    return MovieService().create_movie(db, payload)


@router.get("/", response_model=list[MovieResponse])
def get_movies(db: Session = Depends(get_db)):
    return MovieService().get_movies(db)