from app.domain.entities.base_entity import BaseEntity
from app.domain.entities.card_elements.card_element import CardElement
from app.domain.values.name import Name
from app.domain.values.description import Description
from app.domain.values.entity_id import EntityId
from app.domain.collections.card_element_collection import CardElementCollection
from app.domain.values.metadata import MetaData

class Card(BaseEntity):
    """Domain entity representing a card with elements."""
    
    __slots__ = ("_name", "_description", "_elements")
    
    def __init__(self, metadata: MetaData, name: Name, description: Description, elements: CardElementCollection | None = None):
        super().__init__(metadata)
        self._name = name
        self._description = description
        self._elements = elements if elements else CardElementCollection()

#region Card element management
    #region GETTERS
    @property
    def name(self) -> Name:
        """Get card name."""
        return self._name
    
    @property
    def description(self) -> Description:
        """Get card description."""
        return self._description
    
    @property
    def elements(self) -> tuple[CardElement, ...]:
        """Get card elements."""
        return self._elements.get_all()
    
    def get_element_by_id(self, element_id: EntityId) -> CardElement:
        """Get a card element by its ID."""
        return self._elements.get_by_id(element_id)
    
    def get_element_by_index(self, index: int) -> CardElement:
        """Get a card element by its index."""
        return self._elements.get_by_index(index)
    #endregion
    
    #region CHECKERS
    def check_element_exists_by_id(self, element_id: EntityId) -> bool:
        """Check if a card element exists in the card by its ID."""
        return self._elements.exists_by_id(element_id)
    
    def check_element_exists(self, element: CardElement) -> bool:
        """Check if a card element exists in the card."""
        return self._elements.exists(element)
    #endregion
    
    #region SETTERS
    def append_element(self, element: CardElement) -> None:
        """Append a card element to the card."""
        self._elements.append(element)
        
    def insert_element(self, index: int, element: CardElement) -> None:
        """Insert a card element at a specific index in the card."""
        self._elements.insert(index, element)
    #endregion
    
    #region REMOVERS
    def remove_element(self, element: CardElement) -> None:
        """Remove a card element from the card."""
        self._elements.remove(element)
    
    def remove_element_by_id(self, element_id: EntityId) -> None:
        """Remove a card element from the card by its ID."""
        self._elements.remove_by_id(element_id)
    
    def remove_element_by_index(self, index: int) -> None:
        """Remove a card element from the card by its index."""
        self._elements.remove_by_index(index)
    #endregion
    
    #region MOVERS
    def move_element(self, element: CardElement, new_index: int) -> None:
        """Move a card element to a new index in the card."""
        self._elements.move(element, new_index)
    
    def move_element_by_id(self, element_id: EntityId, new_index: int) -> None:
        """Move a card element to a new index in the card by its ID."""
        element = self.get_element_by_id(element_id)
        self._elements.move(element, new_index)
    
    def move_element_by_index(self, index: int, new_index: int) -> None:
        """Move a card element to a new index in the card by its current index."""
        element = self.get_element_by_index(index)
        self._elements.move(element, new_index)
    #endregion
#endregion