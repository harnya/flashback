from fastapi import APIRouter, Depends
from fastapi import Request
from psycopg2.extensions import connection
import requests

from app.db.session import get_db, Session
from app.models.user import UserRegistration
from app.repositories.postgres.user import UserRepository
from app.services.user import UserService


router = APIRouter()

def get_user_repository(conn: connection = Depends(Session)) -> UserRepository:
    return UserRepository(conn)


@router.post("/register")
def register_user(user: UserRegistration, user_repo: UserRepository = Depends(get_user_repository)):
    user_service = UserService(user_repo)
    return user_service.register_user(user)

@router.get("/user/{email}")
def get_user_profile(email: str, user_repo: UserRepository = Depends(get_user_repository)):
    user_service = UserService(user_repo)
    return user_service.get_user_profile(email)
