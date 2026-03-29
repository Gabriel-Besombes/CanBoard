from app.domain.values.entity_id import EntityId

from abc import ABC, abstractmethod
from datetime import datetime

class MetaData(ABC):
    """Interface to define the base common metadata for all domain entities"""
    
    __slots__ = ("_id", "_created_at", "_created_by",)
    
    @property
    @abstractmethod
    def id(self) -> EntityId:
        pass
    
    @property
    @abstractmethod
    def created_at(self) -> datetime:
        pass
    
    @property
    @abstractmethod
    def created_by(self) -> EntityId:
        pass