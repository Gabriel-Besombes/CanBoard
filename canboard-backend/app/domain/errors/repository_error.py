from app.domain.errors.domain_error import DomainError


class RepositoryError(DomainError):
    """Raised when a repository fails to persist or retrieve domain entities."""

    def __init__(self, message: str | None = None):
        super().__init__(message or "Repository operation failed")
