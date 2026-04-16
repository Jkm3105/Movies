import uuid
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from models.reservation import Reservation
from models.reservation_seat import ReservationSeat

class ReservationService:

    def reserve(self, db, user_id, showtime_id, seat_ids):
        try:
            reservation = Reservation(
                id=str(uuid.uuid4()),
                user_id=user_id,
                showtime_id=showtime_id,
                status="CONFIRMED"
            )
            db.add(reservation)
            db.flush()

            for seat_id in seat_ids:
                db.add(ReservationSeat(
                    id=str(uuid.uuid4()),
                    reservation_id=reservation.id,
                    showtime_id=showtime_id,
                    seat_id=seat_id
                ))

            db.commit()
            return reservation

        except IntegrityError:
            db.rollback()
            raise HTTPException(400, "Seat already booked")