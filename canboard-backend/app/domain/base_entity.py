from abc import ABC
from app.domain.values.entity_id import EntityId
from typing import Optional

class BaseEntity(ABC):
    """Base class for all domain entities."""

    def __init__(self, id: Optional[EntityId] = None):
        if id is None:
            self._id = EntityId.new()
        elif not isinstance(id, EntityId):
            raise TypeError("id must be an EntityId")
        else:
            self._id = id

    @property
    def id(self) -> EntityId:
        return self._id

    def __eq__(self, other):
        return type(self) is type(other) and self.id == other.id

    def __hash__(self):
        return hash((type(self), self.id))

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.id})"