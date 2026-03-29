from dataclasses import dataclass
from app.domain.values.value_compared import ValueCompared


@dataclass(frozen=True)
class UserName(ValueCompared):
    value: str

    def __post_init__(self):
        if not isinstance(self.value, str):
            raise ValueError("User name must be a string")
        
        if not self.value.strip():
            raise ValueError("User name cannot be empty")