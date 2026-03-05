from dataclasses import dataclass
from app.domain.values.entity_id import EntityId


@dataclass
class CardDTO:
    """DTO for Card data."""
    id: EntityId
    name: str
    description: str
    elements: list