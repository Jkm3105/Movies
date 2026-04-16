from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.user import UserResponse
from schemas.auth import SignupRequest, LoginRequest
from services.auth_service import AuthService
from api.deps import get_db

router = APIRouter()
print("AUTH LOADED")


@router.post("/signup", response_model=UserResponse)
def signup(payload: SignupRequest, db: Session = Depends(get_db)):
    service = AuthService()
    user = service.signup(db, payload.email, payload.password)
    return user 

@router.post("/login")
def login(payload: LoginRequest, db: Session = Depends(get_db)):
    service = AuthService()
    token = service.login(db, payload.email, payload.password)

    if not token:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    return {
        "access_token": token,
        "token_type": "bearer"
    }