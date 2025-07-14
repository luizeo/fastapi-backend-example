from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.user_schema import UserCreate, UserRead
from app.services.user_service import register_user, list_users
from app.config.settings import get_db


router = APIRouter()

@router.post("/", response_model=UserRead)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        return register_user(db, user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[UserRead])
def get_users(db: Session = Depends(get_db)):
    return list_users(db)