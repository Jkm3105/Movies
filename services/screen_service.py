from models.screen import Screen
class ScreenService:
    def create_screen(self, db, data):
        screen = Screen(
            name=data.name,
            theatre_id=data.theatre_id
        )
        db.add(screen)
        db.commit()
        db.refresh(screen)
        return screen
    
    def get_screen(self, db):
        return db.query(Screen).all()