from app.domain.base_entity import BaseEntity
from app.domain.column import Column
from app.domain.card import Card
from app.domain.values.name import Name
from app.domain.values.description import Description
from app.domain.values.entity_id import EntityId

class Board(BaseEntity):
    """Board domain entity."""

    def __init__(self, name: Name, description: Description, columns: list[Column] | None = None, id: EntityId | None = None):
        super().__init__(id=id)
        self.name = name
        self.description = description
        self.columns = columns
        
    @property
    def name(self) -> Name:
        return self._name
    
    @name.setter
    def name(self, new_name: Name) -> None:
        if not isinstance(new_name, Name):
            raise ValueError("Name must be a Name instance")
        self._name = new_name
    
    @property
    def description(self) -> Description:
        return self._description
    
    @description.setter
    def description(self, new_description: Description) -> None:
        if not isinstance(new_description, Description):
            raise ValueError("Description must be a Description instance")
        self._description = new_description
        
    @property
    def columns(self) -> list[Column]:
        return self._columns.copy()
    
    @columns.setter
    def columns(self, new_columns: list[Column] | None) -> None:
        if new_columns is None or new_columns == []:
            self._columns = []
            return
        
        if not isinstance(new_columns, list) or not all(isinstance(col, Column) for col in new_columns):
            raise ValueError("Columns must be a list of Column instances")
        self._columns = new_columns
    
    def get_card_by_id(self, card_id: EntityId) -> Card:
        """Get a card by its ID from any column."""
        for column in self._columns:
            try:
                return column.get_card_by_id(card_id)
            except ValueError:
                continue
        raise ValueError(f"Card with id {card_id} not found in any column")
    
    def move_card(self, card_id: EntityId, starting_column_id: EntityId, target_column_id: EntityId, index: int = None) -> None:
        """Move a card between columns."""
        starting_column = self.get_column_by_id(starting_column_id)
        target_column = self.get_column_by_id(target_column_id)

        if not starting_column:
            raise ValueError(f"Starting column with id {starting_column_id} not found")
        if not target_column:
            raise ValueError(f"Target column with id {target_column_id} not found")

        card = starting_column.get_card_by_id(card_id)

        starting_column.remove_card(card)
        if index is not None:
            target_column.insert_card(index, card)
        else:
            target_column.add_card(card)
            
    def add_column(self, column: Column) -> None:
        """Add a column to the board."""
        if not isinstance(column, Column):
            raise ValueError("Column must be a Column instance")
        self._columns.append(column)
        
    def remove_column(self, column_id: EntityId) -> None: # TODO: check if empty
        """Remove a column from the board."""
        column = next((col for col in self._columns if col.id == column_id), None)
        if not column:
            raise ValueError(f"Column with id {column_id} not found")
        self._columns.remove(column)
        
    def insert_column(self, index: int, column: Column) -> None:
        """Insert a column at a specific index in the board."""
        if not isinstance(column, Column):
            raise ValueError("Column must be a Column instance")
        self._columns.insert(index, column)
    
    def get_column_by_id(self, column_id: EntityId) -> Column:
        """Get a column by its ID."""
        column = next((col for col in self._columns if col.id == column_id), None)
        if not column:
            raise ValueError(f"Column with id {column_id} not found")
        return column

    def __repr__(self) -> str:
        return f"Board(id={self.id}, name={self.name}, description={self.description}, columns={self.columns})"
        