from app.domain.base_entity import BaseEntity
from app.domain.values.name import Name
from app.domain.values.description import Description

class Board(BaseEntity):
    """Board domain entity."""

    def __init__(self, id: int, name: Name, description: Description):
        super().__init__(id)
        self.name = name
        self.description = description
        
    @property
    def name(self) -> Name:
        return self._name
    
    @name.setter
    def name(self, new_name: Name):
        if not isinstance(new_name, Name):
            raise ValueError("Name must be a Name instance")
        self._name = new_name
    
    @property
    def description(self) -> Description:
        return self._description
    
    @description.setter
    def description(self, new_description: Description):
        if not isinstance(new_description, Description):
            raise ValueError("Description must be a Description instance")
        self._description = new_description

    def __repr__(self):
        return f"Board(id={self.id}, name={self.name}, description={self.description})"