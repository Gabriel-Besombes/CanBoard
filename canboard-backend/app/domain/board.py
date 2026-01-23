from app.domain.base_entity import BaseEntity

class Board(BaseEntity):
    def __init__(self, id: int, name: str, description: str):
        super().__init__(id)
        self.name = name
        self.description = description