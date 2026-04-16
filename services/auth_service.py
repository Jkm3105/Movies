from models.user import User
from core.security import hash_password, verify_password, create_token

class AuthService:

    def signup(self, db, email, password):
        user = User(
            email=email,
            password_hash=hash_password(password)
        )
        db.add(user)
        db.commit()
        return user

    def login(self, db, email, password):
        user = db.query(User).filter(User.email == email).first()

        if not user or not verify_password(password, user.password_hash):
            return None

        token = create_token({"user_id": user.id})
        return token