import psycopg2
from contextlib import contextmanager
from app.core.config import settings

@contextmanager
def get_db():
    print(settings)
    # conn = psycopg2.connect(host=settings.get('PGHOST'), user=settings.get('PGUSER'),
                            # database=set.get('PGDATABASE'), password=settings.get('PGPASSWORD'))
    conn = psycopg2.connect(host=settings.PGHOST, user=settings.PGUSER, dbname=settings.PGDATABASE,
                            password=settings.PGPASSWORD, options="-c search_path=flash,public")
    # try:
    yield conn
    # finally:
    #     conn.close()

class Session():
    def __init__(self):
       self.conn = None
         
    def __enter__(self):
        conn = psycopg2.connect(host=settings.PGHOST, user=settings.PGUSER, dbname=settings.PGDATABASE,
                            password=settings.PGPASSWORD, options="-c search_path=flash,public")
    
        return conn
     
    def __exit__(self, exc_type, exc_value, exc_traceback):
        # self.conn.cose()
        print('exit method called', exc_type, exc_value, exc_traceback)
 

