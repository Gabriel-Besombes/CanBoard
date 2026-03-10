from datetime import datetime, UTC
from app.domain.values.entity_id import EntityId
from pydantic import BaseModel, ConfigDict, Field

class BaseEntity(BaseModel):
    """Base class for all domain entities."""
    # This propagates through inheritance, so all entities will have these validation rules
    # Hence why frozen=True is not in the config, since some entities may need mutable fields
    model_config = ConfigDict(
        validate_assignment=True, 
        strict=True, 
        extra="forbid", 
        arbitrary_types_allowed=True
    )

    id: EntityId = Field(default_factory=EntityId.new, frozen=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(tz=UTC), frozen=True)
    created_by: EntityId = Field(frozen=True)

    def __eq__(self, other: object) -> bool:
        if type(self) is not type(other):
            return NotImplemented
        return self.id == other.id

    def __hash__(self) -> int:
        return hash((type(self), self.id))