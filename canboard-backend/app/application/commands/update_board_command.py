from dataclasses import dataclass
from uuid import UUID


@dataclass
class UpdateBoardCommand:
    board_id: UUID
    name: str | None
    description: str | None
    requested_by: UUID
