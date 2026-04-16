
from models.showtime import Showtime
from schemas.showtime import ShowtimeCreate
from sqlalchemy.orm import Session

class ShowtimeService:

    def create_showtime(self, db: Session, data: ShowtimeCreate):
        showtime = Showtime(
            movie_id=data.movie_id,
            screen_id=data.screen_id,
            start_time=data.start_time,
            end_time=data.end_time,
            total_seats=data.total_seats,
            price=data.price
        )

        db.add(showtime)
        db.commit()
        db.refresh(showtime)
        return showtime
    
    def get_showtime(self, db):
        return db.query(Showtime).all()