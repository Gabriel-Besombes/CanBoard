from app.domain.entities.base_entity import BaseEntity
from app.domain.values.name import Name
from typing import Any

class CardElement(BaseEntity):
    """Domain entity representing a card element."""
    
    name: Name
    content: Any