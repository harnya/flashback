from typing import Optional
from app.models.user import UserRegistration, UserProfile
from app.repositories.user import UserRepository
from app.services.auth import JWTEncodeDecode, PasswordHashing

jwt_encode_decode =  JWTEncodeDecode()
password_hasshing = PasswordHashing()

class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def register_user(self, user: UserRegistration) -> UserRegistration:
        is_user_exist = self.user_repo.get_user_by_email(user.email)
        if is_user_exist:
            raise Exception("User already exist")
        user.password = password_hasshing.craete_hash(password=user.password)
        return self.user_repo.create_user(user)

    def get_user_profile(self, email: str) -> Optional[UserProfile]:
        user = self.user_repo.get_user_by_email(email)
        if not user:
            raise Exception("User not exist")
        return user
