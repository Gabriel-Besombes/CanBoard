from app.domain.collections.base_entity_collection import BaseEntityCollection
from app.domain.entities.card_elements.card_element import CardElement

class CardElementCollection(BaseEntityCollection[CardElement]):
    """Collection of card elements in a card."""
    _entity_type = CardElement