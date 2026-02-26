from app.domain.base_entity import BaseEntity
from app.domain.card_elements.card_element import CardElement
from app.domain.values.name import Name
from app.domain.values.description import Description
from typing import List

class Card(BaseEntity):
    """Domain entity representing a card with elements."""

    def __init__(self, id: int, name: Name, description: Description, elements: List[CardElement] = None):
        super().__init__(id)
        self._name = name
        self._description = description
        self._elements = elements if elements is not None else []

    @property
    def name(self) -> Name:
        return self._name
    
    @name.setter
    def name(self, new_name: Name):
        if not isinstance(new_name, Name):
            raise ValueError("Name must be a Name instance")
        self._name = new_name

    @property
    def description(self) -> Description:
        return self._description

    @description.setter
    def description(self, new_description: Description):
        if not isinstance(new_description, Description):
            raise ValueError("Description must be a Description instance")
        self._description = new_description
        
    @property
    def elements(self) -> List[CardElement]:
        return self._elements

    def add_element(self, element: CardElement) -> None:
        """Add a card element if it's not already present."""
        if element not in self._elements:
            self._elements.append(element)

    def remove_element(self, element: CardElement) -> None:
        """Remove a card element if it exists."""
        if element in self._elements:
            self._elements.remove(element)

    def move_element(self, element: CardElement, new_index: int) -> None:
        """Move a card element to a new index."""
        if element in self._elements:
            self._elements.remove(element)
            self._elements.insert(new_index, element)

    def __repr__(self):
        return f"Card(id={self.id}, name={self.name}, description={self.description}, elements={self.elements})"