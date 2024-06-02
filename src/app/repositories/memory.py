from typing import Protocol, List
from app.models.memory import Memory, MemoryDetails

class MemoryRepository(Protocol):

    def get_memory_by_id(self, id: str) -> MemoryDetails:
        pass

    def add_memory(self, memory: Memory) -> Memory:
        pass
    
    def all_memories(self) -> List[MemoryDetails]:
        pass