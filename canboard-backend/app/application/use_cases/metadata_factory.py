from app.domain.values.metadata import MetaData
from app.domain.values.entity_id import EntityId

from datetime import datetime, UTC

class MetaDataFactory:
    
    class _MetaData(MetaData):
        
        def __init__(self, id: EntityId, created_at: datetime, created_by: EntityId):
            self._id = id
            self._created_at = created_at
            self._created_by = created_by
            
        @property
        def id(self) -> EntityId:
            return self._id
            
        @property
        def created_at(self) -> datetime:
            return self._created_at
            
        @property
        def created_by(self) -> EntityId:
            return self._created_by
            
    @classmethod
    def create(cls, created_by: EntityId) -> MetaData:
        return cls._MetaData(id = EntityId.new(), created_at = datetime.now(tz=UTC), created_by = created_by)
            
    @classmethod
    def rehydrate(cls, id: EntityId, created_at: datetime, created_by: EntityId) -> MetaData:
        return cls._MetaData(id = id, created_at = created_at, created_by = created_by)