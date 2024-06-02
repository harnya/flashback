

from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Annotated, Optional
from fastapi import File, Form

class MemoryForm(BaseModel):
    memory : str 
    # created_by : Optional[str] = "unknown"
    memory_date : date

    @classmethod
    def as_form(
        cls,
        memory: Annotated[str, Form()],
        # created_by: Annotated[Optional[str], Form(default=None)],
        memory_date: Annotated[date, Form()],
    ):
        return cls(memory=memory, memory_date=memory_date)

class Memory(BaseModel):
    memory : str 
    created_by : str = "unknown"
    memory_date : date
    memory_url : str | None  = ""

class MemoryDetails(BaseModel):
    id: str
    memory : str 
    file_url : str
    created_by : str = "unknown"
    memory_date : date

    
class MemoryLikes(BaseModel):
    memory : str
    liked_by : str

class MemoryComment(BaseModel):
    memory : str
    comment : str
    created_by : str = "unknown"

    

