from models.seat import Seat

class SeatService:

    def create_seat(self, db, payload):
        seat = Seat(
            seat_number=payload.seat_number,
            row=payload.row,
            price=payload.price,
            screen_id=payload.screen_id
        )

        db.add(seat)
        db.commit()
        db.refresh(seat)

        return seat

    def get_seats(self, db):
        return db.query(Seat).all()

    def get_seats_by_screen(self, db, screen_id):
        return db.query(Seat).filter(Seat.screen_id == screen_id).all()