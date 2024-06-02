
from app.repositories.memory import MemoryRepository
from app.models.memory import Memory, MemoryDetails
from typing import List

class MemoryService:

    def __init__(self, memory_repo: MemoryRepository):
        self.memory_repo = memory_repo

    def add_memory(self, memory: Memory, memory_file: bytes | None) -> Memory:
        memory_url = ""
        if not memory_file:
            memory_url = "https://avatars.githubusercontent.com/u/21107732?v=4"
        memory.memory_url = memory_url
    
        return self.memory_repo.add_memory(memory=memory)
    
    def get_all_memories(self) -> List[MemoryDetails]:
        return self.memory_repo.all_memories()
