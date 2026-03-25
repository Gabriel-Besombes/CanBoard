from datetime import datetime
from app.domain.values.entity_id import EntityId
from app.domain.values.metadata import MetaData


class BaseEntity:
    """Base class for all domain entities with immutable data."""
    
    __slots__ = ("_metadata")
    
    def __init__(self, metadata: MetaData):
        self._metadata = metadata
    
    @property
    def metadata(self) -> MetaData:
        """Get the entity's unique identifier."""
        return self._metadata
    
    @property
    def id(self) -> EntityId:
        """Get the entity's unique identifier."""
        return self._metadata.id
    
    @property
    def created_at(self) -> datetime:
        """Get the timestamp when the entity was created."""
        return self._metadata.created_at
    
    @property
    def created_by(self) -> EntityId:
        """Get the ID of who created this entity."""
        return self._metadata.created_by

    def __eq__(self, other: object) -> bool:
        if type(self) is not type(other):
            return NotImplemented
        return self._metadata.id == other._metadata.id

    def __hash__(self) -> int:
        return hash((type(self), self._metadata.id))