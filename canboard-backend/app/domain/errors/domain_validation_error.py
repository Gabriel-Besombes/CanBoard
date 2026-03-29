from app.domain.errors.domain_error import DomainError


class DomainValidationError(DomainError):
    """Raised when a domain invariant or validation rule is violated."""

    def __init__(self, message: str | None = None):
        super().__init__(message or "Domain validation failed")
