import uuid
from models.movie import Movie

class MovieService:

    def create_movie(self, db, data):
        movie = Movie(
            id=str(uuid.uuid4()),
            title=data.title,
            description=data.description,
            poster_url=data.poster_url
        )
        db.add(movie)
        db.commit()
        return movie

    def get_movies(self, db):
        return db.query(Movie).all()