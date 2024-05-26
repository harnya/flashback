from typing import Optional
from app.models.user import UserRegistration, UserProfile
from app.repositories.user import UserRepository

class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def register_user(self, user: UserRegistration) -> UserRegistration:
        return self.user_repo.create_user(user)

    def get_user_profile(self, email: str) -> Optional[UserProfile]:
        user = self.user_repo.get_user_by_email(email)
        return None
