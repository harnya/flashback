import psycopg2
from contextlib import contextmanager
from app.core.config import settings

@contextmanager
def get_db():
    print(settings)
    # conn = psycopg2.connect(host=settings.get('PGHOST'), user=settings.get('PGUSER'),
                            # database=set.get('PGDATABASE'), password=settings.get('PGPASSWORD'))
    conn = psycopg2.connect(host=settings.PGHOST, user=settings.PGUSER, dbname=settings.PGDATABASE,
                            password=settings.PGPASSWORD)
    try:
        yield conn
    finally:
        conn.close()
