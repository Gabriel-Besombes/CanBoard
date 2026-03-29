from app.domain.entities import BaseEntity
from app.domain.values import Name, MetaData
from typing import Any


class CardElement(BaseEntity):
    """Domain entity representing a card element."""
    
    __slots__ = ("_name", "_content",)
    
    def __init__(self, metadata: MetaData, name: Name, content: Any):
        super().__init__(metadata)
        self._name = name
        self._content = content
    
    #region GETTERS
    @property
    def name(self) -> Name:
        return self._name
    @property
    def content(self) -> Any:
        return self._content
    
    #endregion