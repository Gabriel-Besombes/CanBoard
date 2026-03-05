from dataclasses import dataclass
from uuid import UUID


@dataclass
class DeleteBoardCommand:
    board_id: UUID
    requested_by: UUID
