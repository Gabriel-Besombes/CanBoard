from abc import ABC, abstractmethod
from app.domain.entities.board import Board
from app.domain.values.entity_id import EntityId

class BoardRepository(ABC):
    """Abstract repository for Board domain entity."""

    @abstractmethod
    async def save(self, board: Board) -> None:
        """Save a board to the repository."""
        pass

    @abstractmethod
    async def add(self, board: Board) -> None:
        """Add a board to the repository."""
        pass

    @abstractmethod
    async def remove(self, board_id: EntityId) -> None:
        """Remove a board from the repository."""
        pass

    @abstractmethod
    async def find_by_id(self, board_id: EntityId) -> Board | None:
        """Find a board by its ID."""
        pass

    @abstractmethod
    async def find_all(self, limit: int, offset: int) -> list[Board]:
        """Retrieve all boards from the repository."""
        pass
    
    @abstractmethod
    async def exists(self, board_id: EntityId) -> bool:
        """Check if a board exists in the repository."""
        pass