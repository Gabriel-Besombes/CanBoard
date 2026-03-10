from app.domain.entities.base_entity import BaseEntity
from app.domain.entities.card import Card
from app.domain.values.name import Name
from app.domain.values.description import Description
from app.domain.values.entity_id import EntityId
from app.domain.collections.card_collection import CardCollection
from pydantic import PrivateAttr

class Column(BaseEntity):
    """Represents a column domain entity containing cards."""
    
    name: Name
    description: Description
    _cards: CardCollection = PrivateAttr(default_factory=CardCollection)
    
#region Card management
    #region GETTERS
    @property
    def cards(self) -> tuple[Card, ...]:
        """Get column cards."""
        return self._cards.get_all()
    
    def get_card_by_id(self, card_id: EntityId) -> Card:
        """Get a card from the column by its ID."""
        return self._cards.get_by_id(card_id)
    
    def get_card_by_index(self, index: int) -> Card:
        """Get a card from the column by its index."""
        return self._cards.get_by_index(index)
    #endregion
    
    #region CHECKERS
    def check_card_exists_by_id(self, card_id: EntityId) -> bool:
        """Check if a card exists in the column by its ID."""
        return self._cards.exists_by_id(card_id)
    
    def check_card_exists(self, card: Card) -> bool:
        """Check if a card exists in the column."""
        return self._cards.exists(card)
    #endregion

    #region SETTERS
    def append_card(self, card: Card) -> None:
        """Append a card to the column."""
        self._cards.append(card)
            
    def insert_card(self, index: int, card: Card) -> None:
        """Insert a card at a specific index in the column."""
        self._cards.insert(index, card)
    #endregion

    #region REMOVERS
    def remove_card(self, card: Card) -> None:
        """Remove a card from the column."""
        self._cards.remove(card)
        
    def remove_card_by_id(self, card_id: EntityId) -> None:
        """Remove a card from the column by its ID."""
        self._cards.remove_by_id(card_id)
        
    def remove_card_by_index(self, index: int) -> None:
        """Remove a card from the column by its index."""
        self._cards.remove_by_index(index)
    #endregion

    #region MOVERS
    def move_card(self, card: Card, new_index: int) -> None:
        """Move a card to a new position in the column."""
        self._cards.move(card, new_index)
    
    def move_card_by_id(self, card_id: EntityId, new_index: int) -> None:
        """Move a card to a new position in the column by its ID."""
        self._cards.move_by_id(card_id, new_index)
    
    def move_card_by_index(self, index: int, new_index: int) -> None:
        """Move a card to a new position in the column by its index."""
        self._cards.move_by_index(index, new_index)
    #endregion
#endregion