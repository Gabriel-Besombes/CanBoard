__all__ = (
    "CardElement",
    "TextField",
    "UserListField"
)


def __getattr__(name: str):
    if name == "CardElement":
        from .card_element import CardElement
        return CardElement
    if name == "TextField":
        from .text_field import TextField
        return TextField
    if name == "UserListField":
        from .user_list_field import UserListField
        return UserListField
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


def __dir__():
    return list(__all__)
