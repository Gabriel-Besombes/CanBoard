from dataclasses import dataclass
from uuid import UUID


@dataclass
class RestoreBoardCommand:
    board_id: UUID
    requested_by: UUID
