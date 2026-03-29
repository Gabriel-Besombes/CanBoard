__all__ = (
    "BaseEntityCollection",
    "CardCollection",
    "ColumnCollection",
    "UserCollection",
    "CardElementCollection"
)


def __getattr__(name: str):
    if name == "BaseEntityCollection":
        from .base_entity_collection import BaseEntityCollection
        return BaseEntityCollection
    if name == "CardCollection":
        from .card_collection import CardCollection
        return CardCollection
    if name == "ColumnCollection":
        from .column_collection import ColumnCollection
        return ColumnCollection
    if name == "UserCollection":
        from .user_collection import UserCollection
        return UserCollection
    if name == "CardElementCollection":
        from .card_element_collection import CardElementCollection
        return CardElementCollection
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__():
    return list(__all__)
