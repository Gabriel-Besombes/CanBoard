__all__ = (
    "BaseEntity",
    "Board",
    "Card",
    "Column",
    "User"
)


def __getattr__(name: str):
    if name == "BaseEntity":
        from .base_entity import BaseEntity
        return BaseEntity
    if name == "Board":
        from .board import Board
        return Board
    if name == "Card":
        from .card import Card
        return Card
    if name == "Column":
        from .column import Column
        return Column
    if name == "User":
        from .user import User
        return User
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__():
    return list(__all__)