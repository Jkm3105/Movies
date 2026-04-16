from fastapi import APIRouter, Depends
from models.user import User
from api.deps import get_current_user
from schemas.user import UserResponse

router = APIRouter(prefix="/user", tags=["User"])

@router.get("/me", response_model=UserResponse)
def get_profile(current_user: User = Depends(get_current_user)):
    return current_user