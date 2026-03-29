from app.domain.values.entity_id import EntityId

from abc import ABC, abstractmethod
from datetime import datetime

class MetaData(ABC):
    """Interface to define the base common metadata for all domain entities"""
    
    __slots__ = ("_id", "_created_at", "_created_by",)
    
    @abstractmethod
    @property
    def id(self) -> EntityId:
        pass
    
    @abstractmethod
    @property
    def created_at(self) -> datetime:
        pass
    
    @abstractmethod
    @property
    def created_by(self) -> EntityId:
        pass