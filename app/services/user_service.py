from sqlalchemy.orm import Session
from app.repositories.user_repository import create_user, get_user_by_email
from app.repositories.user_repository import list_users as list_users_repo
from app.schemas.user_schema import UserCreate

def register_user(db: Session, user_data: UserCreate):
    existing_user = get_user_by_email(db, user_data.email)
    if existing_user:
        raise ValueError("Usuário já cadastrado com esse e-mail.")
    return create_user(db, user_data)

def list_users(db: Session):
    return list_users_repo(db)

