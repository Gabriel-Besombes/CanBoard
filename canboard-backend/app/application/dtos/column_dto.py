from dataclasses import dataclass
from app.domain.values.entity_id import EntityId
from app.application.dtos.card_dto import CardDTO


@dataclass
class ColumnDTO:
    """DTO for Column data."""
    id: EntityId
    name: str
    description: str
    cards: list[CardDTO]