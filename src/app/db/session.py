import psycopg2
import psycopg2.extras
from app.core.config import settings

class Session():
    def __init__(self):
       self.conn = None
         
    def __enter__(self):
        conn = psycopg2.connect(host=settings.PGHOST, user=settings.PGUSER, dbname=settings.PGDATABASE,
                            password=settings.PGPASSWORD, options="-c search_path=memory,public",
                            cursor_factory = psycopg2.extras.DictCursor)
    
        return conn
     
    def __exit__(self, exc_type, exc_value, exc_traceback):
        # self.conn.cose()
        print('exit method called', exc_type, exc_value, exc_traceback)
 


