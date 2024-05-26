from psycopg2.extensions import connection
from app.models.user import UserRegistration
from typing import Optional


class UserRepository:
    def __init__(self, conn: connection):
        self.connection = conn

    def get_user_by_email(self, email: str) -> Optional[UserRegistration]:
        with self.connection as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, email, password, auth_group_id FROM users WHERE email = %s", (email,))
            result = cursor.fetchone()
            if result:
                return UserRegistration(id=result[0], email=result[1], password=result[2], auth_group_id=result[3])
            return None

    def create_user(self, user: UserRegistration) -> UserRegistration:
        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO users (id, email, password, auth_group_id) VALUES (%s, %s, %s, %s)",
            (user.id, user.email, user.password, user.auth_group_id)
        )
        self.connection.commit()
        cursor.close()
        return user
