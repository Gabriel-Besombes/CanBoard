from app.domain.entities.base_entity import BaseEntity
from app.domain.entities.column import Column
from app.domain.entities.card import Card
from app.domain.values.name import Name
from app.domain.values.description import Description
from app.domain.values.entity_id import EntityId
from app.domain.collections.column_collection import ColumnCollection
from app.domain.values.metadata import MetaData


class Board(BaseEntity):
    """Board domain entity."""
    
    __slots__ = ("_name", "_description", "_columns")
    
    def __init__(self, metadata: MetaData, name: Name, description: Description, columns: ColumnCollection | None = None):
        super().__init__(metadata)
        self._name = name
        self._description = description
        self._columns = columns if columns else ColumnCollection()
    
#region Column management
    #region GETTERS
    @property
    def name(self) -> Name:
        return self._name
    
    @property
    def description(self) -> Description:
        return self._description
    
    @property
    def columns(self) -> tuple[Column, ...]:
        """Get board columns."""
        return self._columns.get_all()

    def get_column_by_id(self, column_id: EntityId) -> Column:
        """Get a column by its ID."""
        return self._columns.get_by_id(column_id) 
    
    def get_column_by_index(self, index: int) -> Column:
        """Get a column by its index."""
        return self._columns.get_by_index(index)
    #endregion
    
    #region CHECKERS
    def check_column_exists_by_id(self, column_id: EntityId) -> bool:
        """Check if a column exists in the board by its ID."""
        return self._columns.exists_by_id(column_id)
    
    def check_column_exists(self, column: Column) -> bool:
        """Check if a column exists in the board."""
        return self._columns.exists(column)
    #endregion
    
    #region SETTERS
    def append_column(self, column: Column) -> None:
        """Append a column to the board."""
        self._columns.append(column)
        
    def insert_column(self, index: int, column: Column) -> None:
        """Insert a column at a specific index in the board."""
        self._columns.insert(index, column)
    #endregion
        
    #region REMOVERS
    def remove_column(self, column: Column) -> None:
        """Remove a column from the board."""
        self._columns.remove(column)
        
    def remove_column_by_id(self, column_id: EntityId) -> None:
        """Remove a column from the board by its ID."""
        self._columns.remove_by_id(column_id)
        
    def remove_column_by_index(self, index: int) -> None:
        """Remove a column from the board by its index."""
        self._columns.remove_by_index(index)
    #endregion

    #region MOVERS
    def move_column(self, column: Column, new_index: int) -> None:
        """Move a column to a new position in the board."""
        self._columns.move(column, new_index)
        
    def move_column_by_id(self, column_id: EntityId, new_index: int) -> None:
        """Move a column to a new position in the board by its ID."""
        self._columns.move_by_id(column_id, new_index)
    
    def move_column_by_index(self, index: int, new_index: int) -> None:
        """Move a column to a new position in the board by its index."""
        self._columns.move_by_index(index, new_index)
    #endregion
#endregion

#region Card management
    def _find_column_containing_card(self, card_id: EntityId) -> Column:
        for column in self.columns:
            if column.check_card_exists_by_id(card_id):
                return column
        raise ValueError(f"Card with id {card_id} not found in board {self.id}")
            
    #region GETTERS
    def get_card_by_id(self, card_id: EntityId) -> Card:
        """Get a card by its ID from any column."""
        return self._find_column_containing_card(card_id = card_id).get_card_by_id(card_id)
    #endregion
    
    #region CHECKERS
    def check_card_exists(self, card: Card) -> bool:
        """Check if a card exists in the board."""
        return any(column.check_card_exists(card) for column in self.columns)
    
    def check_card_exists_by_id(self, card_id: EntityId) -> bool:
        """Check if a card exists in the board by its ID."""
        return any(column.check_card_exists_by_id(card_id) for column in self.columns)
    #endregion
    
    #region SETTERS
    def append_card(self, card: Card, column_id: EntityId) -> None:
        """Append a card to a specific column in the board."""
        column = self.get_column_by_id(column_id)
        column.append_card(card)
    
    def insert_card(self, index: int, card: Card, column_id: EntityId) -> None:
        """Insert a card at a specific index in a specific column in the board."""
        column = self.get_column_by_id(column_id)
        column.insert_card(index, card)
    #endregion
    
    #region REMOVERS
    def remove_card(self, card: Card) -> None:
        """Remove a card from the board."""
        for column in self.columns:
            if column.check_card_exists(card):
                column.remove_card(card)
                return
        raise ValueError(f"{card} not found in board {self.id}")
    
    def remove_card_by_id(self, card_id: EntityId) -> None:
        """Remove a card from the board by its ID."""
        self._find_column_containing_card(card_id=card_id).remove_card_by_id(card_id=card_id)
    
    def remove_card_by_index(self, index: int, column_id: EntityId) -> None:
        """Remove a card from the board by its index in a specific column."""
        column = self.get_column_by_id(column_id)
        column.remove_card_by_index(index)
    #endregion

    #region MOVERS
    def move_card(self, card: Card, starting_column_id: EntityId, target_column_id: EntityId, target_index: int = None) -> None:
        """Move a card between columns."""
        starting_column = self.get_column_by_id(starting_column_id)
        target_column = self.get_column_by_id(target_column_id)
        starting_column.remove_card(card)
        if target_index is not None:
            target_column.insert_card(target_index, card)
        else:
            target_column.append_card(card)
    
    def move_card_by_id(self, card_id: EntityId, starting_column_id: EntityId, target_column_id: EntityId, target_index: int = None) -> None:
        """Move a card between columns by its ID."""
        starting_column = self.get_column_by_id(starting_column_id)
        target_column = self.get_column_by_id(target_column_id)
        card = starting_column.get_card_by_id(card_id)
        starting_column.remove_card_by_id(card_id)
        if target_index is not None:
            target_column.insert_card(target_index, card)
        else:
            target_column.append_card(card)
    
    def move_card_by_index(self, index: int, starting_column_id: EntityId, target_column_id: EntityId, target_index: int = None) -> None:
        """Move a card between columns by its index in the starting column."""
        starting_column = self.get_column_by_id(starting_column_id)
        target_column = self.get_column_by_id(target_column_id)
        card = starting_column.get_card_by_index(index)
        starting_column.remove_card_by_index(index)
        if target_index is not None:
            target_column.insert_card(target_index, card)
        else:
            target_column.append_card(card)
    #endregion
#endregion