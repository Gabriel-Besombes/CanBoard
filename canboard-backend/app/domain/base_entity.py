from abc import ABC

class BaseEntity(ABC):
    """Base class for all domain entities."""

    def __init__(self, id: int):
        if not isinstance(id, int):
            raise TypeError("id must be an integer")
        if id <= 0:
            raise ValueError("id must be a positive integer")
        self._id = id

    @property
    def id(self) -> int:
        return self._id

    def __eq__(self, other):
        if not isinstance(other, BaseEntity):
            return NotImplemented
        return type(self) is type(other) and self.id == other.id

    def __hash__(self):
        return hash((type(self), self.id))

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.id})"