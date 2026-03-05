from app.domain.base_entity import BaseEntity
from app.domain.card import Card
from app.domain.values.name import Name
from app.domain.values.description import Description
from app.domain.values.entity_id import EntityId
from typing import List, Optional

class Column(BaseEntity):
    """Represents a column domain entity containing cards."""

    def __init__(self, name: Name, description: Description, cards: Optional[List[Card]] = None, id: Optional[EntityId] = None):
        super().__init__(id=id)
        self.name = name
        self.description = description
        self.cards = cards
        
    @property
    def name(self) -> Name:
        return self._name
    
    @name.setter
    def name(self, new_name: Name) -> None:
        if not isinstance(new_name, Name):
            raise ValueError("Name must be a Name instance")
        self._name = new_name
        
    @property
    def description(self) -> Description:
        return self._description
    
    @description.setter
    def description(self, new_description: Description) -> None:
        if not isinstance(new_description, Description):
            raise ValueError("Description must be a Description instance")
        self._description = new_description
        
    @property
    def cards(self) -> list[Card]:
        return self._cards.copy()
    
    @cards.setter
    def cards(self, new_cards: Optional[List[Card]]) -> None:
        if new_cards is None or new_cards == []:
            self._cards = []
            return
        
        if not isinstance(new_cards, list) or not all(isinstance(card, Card) for card in new_cards):
            raise ValueError("Cards must be a list of Card instances")
        self._cards = new_cards

    def add_card(self, card: Card) -> None:
        """Add a card to the column if it is not already present."""
        if card not in self.cards:
            self._cards.append(card)

    def remove_card(self, card: Card) -> None:
        """Remove a card from the column if it exists."""
        if card in self.cards:
            self._cards.remove(card)

    def move_card(self, card: Card, new_index: int) -> None:
        """Move a card to a new position in the column."""
        if card in self.cards:
            self._cards.remove(card)
            self._cards.insert(new_index, card)
        else:
            raise ValueError(f"Card {card} not found in column")
            
    def insert_card(self, index: int, card: Card) -> None:
        """Insert a card at a specific index in the column."""
        if not isinstance(index, int) or index < 0 or index > len(self.cards):
            raise ValueError("Index must be a non-negative integer within the bounds of the cards list")
        if not isinstance(card, Card):
            raise ValueError("Card must be a Card instance")
        self._cards.insert(index, card)
    
    def get_card_by_id(self, card_id: EntityId) -> Card:
        """Get a card from the column by its ID."""
        for card in self.cards:
            if card.id == card_id:
                return card
        raise ValueError(f"Card with id {card_id} not found in column with id {self.id}")

    def __repr__(self) -> str:
        return f"Column(id={self.id}, name={self.name}, description={self.description}, cards={self.cards})"