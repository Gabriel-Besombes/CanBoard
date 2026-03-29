from dataclasses import dataclass
from app.domain.values.value_compared import ValueCompared


@dataclass(frozen=True)
class PasswordHash(ValueCompared):
    value: int

    def __post_init__(self):
        if not isinstance(self.value, int):
            raise ValueError("PasswordHash must be an int")