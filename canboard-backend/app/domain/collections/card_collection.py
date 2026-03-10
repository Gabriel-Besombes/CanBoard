from app.domain.collections.base_entity_collection import BaseEntityCollection
from app.domain.entities.card import Card

class CardCollection(BaseEntityCollection[Card]):
    """Collection of cards in a column."""
    _entity_type = Card