from dataclasses import dataclass
from uuid import UUID


@dataclass
class ArchiveBoardCommand:
    board_id: UUID
    requested_by: UUID
