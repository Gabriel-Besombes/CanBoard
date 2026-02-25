from app.domain.base_entity import BaseEntity
from app.domain.card_elements.card_element import CardElement
from typing import List

class Card(BaseEntity):
    """Domain entity representing a card with elements."""

    def __init__(self, id: int, name: str, description: str, elements: List[CardElement] = None):
        super().__init__(id)
        self._name = name
        self._description = description
        self._elements = elements if elements is not None else []

    @property
    def name(self) -> str:
        return self._name

    @property
    def description(self) -> str:
        return self._description

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