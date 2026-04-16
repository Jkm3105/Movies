from models.theatre import Theatre

class TheatreService:
    def create_theatre(self, db, data):
        theatre = Theatre(
            name=data.name,
            location=data.location
        )
        db.add(theatre)
        db.commit()
        db.refresh(theatre)
        return theatre
    
    def get_theatre(self, db):
        return db.query(Theatre).all()