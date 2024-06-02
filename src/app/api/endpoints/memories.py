from fastapi import APIRouter, Depends, HTTPException, File, UploadFile
from psycopg2.extensions import connection
from app.repositories.postgres.memory import MemoryRepository
from app.services.memory import MemoryService
from app.models.memory import MemoryForm, Memory
from typing import Annotated, Optional


from app.db.session import Session

router = APIRouter()


def get_memory_repository(conn:connection = Depends(Session)) -> MemoryRepository:
    return MemoryRepository(conn)

@router.post("/memory/add_memory")
async def create_file(
    memory_details: Annotated[MemoryForm, Depends(MemoryForm.as_form)],
    memory_repo: MemoryRepository = Depends(get_memory_repository),
    memory_file: Annotated[UploadFile, File()] = None,
    ):
    memory_service = MemoryService(memory_repo=memory_repo)
    memory = Memory(**memory_details.dict())
    memory_service.add_memory(memory=memory, memory_file=memory_file)
    
    return {
        "your memory added in a book"
    }


@router.get("/memory/")
def all_memories(memory_repo: MemoryRepository = Depends(get_memory_repository)):
    memory_service = MemoryService(memory_repo=memory_repo)
    return memory_service.get_all_memories()
