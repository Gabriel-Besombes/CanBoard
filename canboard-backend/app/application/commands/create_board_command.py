from dataclasses import dataclass
from uuid import UUID


@dataclass
class CreateBoardCommand:
    name: str
    description: str | None
    owner_id: UUID
    requested_by: UUID