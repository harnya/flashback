from typing import Protocol

from app.models.user import UserRegistration, UserProfile

class UserRepository(Protocol):
    def get_user_by_email(self, email: str) -> UserRegistration:
        pass
    
    def create_user(self, user: UserRegistration) -> UserRegistration:
        pass

    def get_user_password(self, email: str) -> str:
        pass

