from dataclasses import dataclass
from app.domain.values.value_compared import ValueCompared


@dataclass(frozen=True)
class Name(ValueCompared):
    value: str

    def __post_init__(self):
        if not isinstance(self.value, str):
            raise ValueError("Name must be a string")
        
        if not self.value.strip():
            raise ValueError("Name cannot be empty")