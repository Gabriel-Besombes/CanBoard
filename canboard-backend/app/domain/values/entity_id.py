from uuid import uuid7, UUID
from dataclasses import dataclass
from app.domain.values.value_compared import ValueCompared

@dataclass(frozen=True)
class EntityId(ValueCompared):
    value: UUID
    
    @staticmethod
    def new() -> EntityId:
        return EntityId(uuid7())
    
    def __post_init__(self):
        if not isinstance(self.value, UUID):
            raise ValueError("value must be a UUID")
        if self.value.version != 7:
            raise ValueError("Must be UUIDv7")