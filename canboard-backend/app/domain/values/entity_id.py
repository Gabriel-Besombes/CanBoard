from uuid import uuid7, UUID
from dataclasses import dataclass

@dataclass(frozen=True)
class EntityId:
    value: UUID
    
    @staticmethod
    def new() -> EntityId:
        return EntityId(uuid7())
    
    def __post_init__(self):
        if self.value.version != 7:
            raise ValueError("Must be UUIDv7")