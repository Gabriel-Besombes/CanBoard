from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass(frozen=True)
class ValueCompared(ABC):
    
    @property
    @abstractmethod
    def value(self):
        pass
    
    def __eq__(self, other: ValueCompared) -> bool:
        return isinstance(other, self.__class__) and self.value == other.value