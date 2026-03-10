from typing import Generic, TypeVar, Iterable
from app.domain.values.entity_id import EntityId

T = TypeVar("T")

class BaseEntityCollection(Generic[T]):
    
    _entity_type: type
    
    def __init__(self, items: Iterable[T] | None = None):
        self._items: list[T] = list(items or [])

#region GETTERS
    def get_all(self) -> tuple[T, ...]: # using tuple for immutability, since we want to control how items are added/removed/updated through methods
        return tuple(self._items)

    def get_by_id(self, entity_id: EntityId) -> T:
        for item in self._items:
            if item.id == entity_id:
                return item
        raise ValueError(f"Entity with id {entity_id} not found")
    
    def get_by_index(self, index: int) -> T:
        try:
            return self._items[index]
        except IndexError:
            raise ValueError(f"Index {index} out of range")
#endregion

#region CHECKERS
    def _validate_entity_type(self, item: T) -> None:
        if not isinstance(item, self._entity_type):
            raise TypeError(f"{item} must be an instance of {self._entity_type.__name__}")
        
    def exists(self, item: T) -> bool:
        self._validate_entity_type(item)
        return item in self._items

    def exists_by_id(self, entity_id: EntityId) -> bool:
        return any(item.id == entity_id for item in self._items)
#endregion

#region SETTERS
    def append(self, item: T) -> None:
        self._validate_entity_type(item)
        if item in self._items:
            raise ValueError(f"{item} already exists")
        self._items.append(item)

    def insert(self, index: int, item: T) -> None:
        self._validate_entity_type(item)
        if item in self._items:
            raise ValueError(f"{item} already exists")
        self._items.insert(index, item)
#endregion

#region REMOVERS
    def remove(self, item: T) -> None:
        self._validate_entity_type(item)
        if item not in self._items:
            raise ValueError(f"{item} not found")
        self._items.remove(item)
        
    def remove_by_id(self, entity_id: EntityId) -> None:
        item = self.get_by_id(entity_id)
        self.remove(item)
        
    def remove_by_index(self, index: int) -> None:
        item = self.get_by_index(index)
        self.remove(item)
#endregion

#region MOVERS
    def move(self, item: T, new_index: int) -> None:
        self._validate_entity_type(item)
        self.remove(item)
        self._items.insert(new_index, item)
        
    def move_by_id(self, entity_id: EntityId, new_index: int) -> None:
        item = self.get_by_id(entity_id)
        self.move(item, new_index)
    
    def move_by_index(self, index: int, new_index: int) -> None:
        item = self.get_by_index(index)
        self.move(item, new_index)
#endregion