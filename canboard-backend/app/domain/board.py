from app.domain.base_entity import BaseEntity

class Board(BaseEntity):
    """Board domain entity."""

    def __init__(self, id: int, name: str, description: str):
        super().__init__(id)
        self.name = name
        self.description = description

    def __repr__(self):
        return f"Board(id={self.id}, name={self.name}, description={self.description})"