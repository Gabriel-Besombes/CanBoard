from abc import ABC
from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True)
class ValueCompared(ABC):
    value: Any
    
    def __eq__(self, other: ValueCompared) -> bool:
        return isinstance(other, self.__class__) and self.value == other.value