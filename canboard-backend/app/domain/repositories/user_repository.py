from abc import ABC, abstractmethod
from app.domain.entities.user import User
from app.domain.values.email import Email
from app.domain.values.entity_id import EntityId
from app.domain.values.user_name import UserName


class UserRepository(ABC):
    """Abstract repository for User domain entity."""

    @abstractmethod
    async def save(self, user: User) -> None:
        """Save a user to the repository."""
        pass

    @abstractmethod
    async def add(self, user: User) -> None:
        """Add a new user to the repository."""
        pass

    @abstractmethod
    async def remove(self, user_id: EntityId) -> None:
        """Remove a user from the repository."""
        pass

    @abstractmethod
    async def find_by_id(self, user_id: EntityId) -> User | None:
        """Find a user by its ID."""
        pass

    @abstractmethod
    async def find_by_email(self, email: Email) -> User | None:
        """Find a user by email."""
        pass

    @abstractmethod
    async def find_by_user_name(self, user_name: UserName) -> User | None:
        """Find a user by user name."""
        pass

    @abstractmethod
    async def find_all(self, limit: int, offset: int) -> list[User]:
        """Retrieve all users from the repository."""
        pass

    @abstractmethod
    async def exists(self, user_id: EntityId) -> bool:
        """Check if a user exists in the repository."""
        pass
