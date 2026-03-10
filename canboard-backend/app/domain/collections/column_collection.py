from app.domain.collections.base_entity_collection import BaseEntityCollection
from app.domain.entities.column import Column

class ColumnCollection(BaseEntityCollection[Column]):
    """Collection of columns in a board."""
    _entity_type = Column