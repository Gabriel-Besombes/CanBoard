from app.domain.base_entity import BaseEntity
from app.domain.card import Card

class Column(BaseEntity):
    """Represents a column domain entity containing cards."""

    def __init__(self, id: int, name: str, description: str, cards: list[Card] = None):
        super().__init__(id)
        self.name = name
        self.description = description
        self.cards = cards if cards is not None else []

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