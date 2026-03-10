from app.domain.base_entity import BaseEntity
from app.domain.values.name import Name
from app.domain.values.entity_id import EntityId
from abc import ABC

class CardElement(BaseEntity, ABC):
    """Domain entity representing a card element."""
    
    def __init__(self, name: Name, content: object, id: EntityId | None = None):
        """
        Initialize a CardElement.
        
        Args:
            id: The unique identifier for the card element.
            name: The name of the card element.
            content: The content of the card element, can be of any type depending on the specific element.
        """
        super().__init__(id=id)
        self._name = name
        self._content = content
        
    @property
    def name(self) -> Name:
        return self._name
    
    @name.setter
    def name(self, new_name: Name):
        if not isinstance(new_name, Name):
            raise ValueError("Name must be a Name instance")
        self._name = new_name

    @property
    def content(self):
        return self._content

    def __repr__(self):
        return f"CardElement(id={self.id}, name={self.name}, content={self.content})"