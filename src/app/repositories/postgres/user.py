from psycopg2.extensions import connection
from app.models.user import UserRegistration
from typing import Optional


class UserRepository:
    def __init__(self, conn: connection):
        self.connection = conn

    def get_user_by_email(self, email: str) -> Optional[UserRegistration]:
        with self.connection as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, email, password FROM AUTH WHERE email = %s", (email,))
            result = cursor.fetchone()
            if result:
                return UserRegistration(id=result[0], email=result[1], password=result[2])
            return None

    def create_user(self, user: UserRegistration) -> UserRegistration:
        with self.connection as conn:
            cursor = conn.cursor()
            # cursor.execute(
            #     "INSERT INTO AUTH (id, email, password) VALUES (%s, %s, %s)",
            #     (str(user.id), user.email, user.password)
            # )
            insert_query = f"INSERT INTO AUTH (id, email, password) VALUES ('{str(user.id)}','{user.email}','{user.password}')"
            cursor.execute(insert_query)
            conn.commit()  

        return user
