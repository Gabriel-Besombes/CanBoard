from app.domain.base_entity import BaseEntity
from app.domain.card import Card
from app.domain.values.name import Name
from app.domain.values.description import Description

class Column(BaseEntity):
    """Represents a column domain entity containing cards."""

    def __init__(self, id: int, name: Name, description: Description, cards: list[Card] = None):
        super().__init__(id)
        self.name = name
        self.description = description
        self.cards = cards if cards is not None else []
        
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

    def add_card(self, card: Card) -> None:
        """Add a card to the column if it is not already present."""
        if card not in self.cards:
            self.cards.append(card)

    def remove_card(self, card: Card) -> None:
        """Remove a card from the column if it exists."""
        if card in self.cards:
            self.cards.remove(card)

    def move_card(self, card: Card, new_index: int) -> None:
        """Move a card to a new position in the column."""
        if card in self.cards:
            self.cards.remove(card)
            self.cards.insert(new_index, card)

    def __repr__(self):
        return f"Column(id={self.id}, name={self.name}, description={self.description}, cards={self.cards})"