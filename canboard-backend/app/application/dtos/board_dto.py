from dataclasses import dataclass
from app.domain.values.entity_id import EntityId
from app.application.dtos.column_dto import ColumnDTO


@dataclass
class BoardDTO:
    """Output DTO for Board commands."""
    id: EntityId
    name: str
    description: str
    columns: list[ColumnDTO]