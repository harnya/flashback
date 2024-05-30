from fastapi import APIRouter, Depends
from psycopg2.extensions import connection
from fastapi import Request, HTTPException
import requests

from app.db.session import Session
from app.models.user import UserRegistration
from app.repositories.postgres.user import UserRepository
from app.services.user import UserService


router = APIRouter()

def get_user_repository(conn:connection = Depends(Session)) -> UserRepository:
    return UserRepository(conn)


@router.post("/register")
def register_user(user: UserRegistration, user_repo: UserRepository = Depends(get_user_repository)):
    user_service = UserService(user_repo)
    return user_service.register_user(user)

@router.get("/user/{email}")
def get_user_profile(email: str, user_repo: UserRepository = Depends(get_user_repository)):
    user_service = UserService(user_repo)
    try:
        user_profile = user_service.get_user_profile(email)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    return user_profile

@router.post("/user/login")
def login_user(email: str, password:str, user_repo: UserRepository = Depends(get_user_repository)):
    user_service = UserService(user_repo)
    try:
        login_user = user_service.login_user(email, password)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    if not login_user:
        raise HTTPException(status_code=403, detail=str("unautherise user"))
    return login_user

