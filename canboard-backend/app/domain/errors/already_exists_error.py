from app.domain.errors.domain_error import DomainError


class AlreadyExistsError(DomainError):
    """Raised when an entity already exists in an aggregate or repository."""

    def __init__(self, entity_type: str | None = None, identifier: object | None = None, message: str | None = None):
        if message is None:
            if entity_type and identifier is not None:
                message = f"{entity_type} with id {identifier} already exists"
            elif entity_type:
                message = f"{entity_type} already exists"
            else:
                message = "Entity already exists"
        super().__init__(message)
