from psycopg2.extensions import connection
import psycopg2.extras

from app.models.user import UserRegistration, UserProfile
from typing import Optional


class UserRepository:
    def __init__(self, conn: connection):
        self.connection = conn

    def get_user_by_email(self, email: str) -> Optional[UserProfile]:
        with self.connection as conn:
            cursor = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
            cursor.execute("SELECT id, email, is_active, first_name, last_name, created_at FROM AUTH WHERE email = %s", (email,))
            result = cursor.fetchone()
            if result:
                return UserProfile(**result)
            return None

    def create_user(self, user: UserRegistration) -> UserRegistration:
        with self.connection as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO AUTH (email, password) VALUES (%s, %s)",
                (user.email, user.password)
            )
            conn.commit()  
        return user
