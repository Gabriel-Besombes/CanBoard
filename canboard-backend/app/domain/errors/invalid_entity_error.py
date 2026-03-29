from app.domain.errors.domain_error import DomainError


class InvalidEntityError(DomainError):
    """Raised when an entity is not valid for the current operation."""

    def __init__(self, expected_type: str | None = None, actual: object | None = None, message: str | None = None):
        if message is None:
            if expected_type and actual is not None:
                message = f"Expected entity of type {expected_type}, got {type(actual).__name__}"
            elif expected_type:
                message = f"Expected entity of type {expected_type}"
            else:
                message = "Invalid entity"
        super().__init__(message)
