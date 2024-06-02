from psycopg2.extensions import connection
import psycopg2.extras
from app.models.memory import Memory, MemoryDetails
from typing import List


class MemoryRepository:
    def __init__(self, conn: connection):
        self.connection = conn
        
    def add_memory(self, memory: Memory) -> Memory:
        with self.connection as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO MEMORY (memory, memory_date, file_url, created_by) 
                VALUES (%s, %s, %s,(SELECT id FROM auth WHERE email=%s))
                """,
                (memory.memory, memory.memory_date, memory.memory_url, memory.created_by)
            )
            conn.commit()  
        return memory
    
    def all_memories(self) -> List[MemoryDetails]:
        result = {}
        with self.connection as conn:
            cursor = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
            cursor.execute(
            """
            select m.id, memory, memory_date, file_url, email as created_by from memory as m 
            join auth as a on m.created_by = a.id 
            where m.is_active=true;
            """
                )
        result = cursor.fetchall()
        return [MemoryDetails(**i) for i in result]
