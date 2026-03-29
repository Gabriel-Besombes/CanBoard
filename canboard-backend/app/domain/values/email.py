from dataclasses import dataclass
from app.domain.values.value_compared import ValueCompared


@dataclass(frozen=True)
class Email(ValueCompared):
    value: str

    def __post_init__(self):
        if not isinstance(self.value, str):
            raise ValueError("Email must be a string")
        
        if not self.value.strip():
            raise ValueError("Email cannot be empty")
        
        if "@" not in self.value:
            raise ValueError("Must be a valid email")
