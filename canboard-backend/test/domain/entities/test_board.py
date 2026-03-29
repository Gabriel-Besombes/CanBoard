from app.domain.entities.board import Board

"""
Tests for the Board domain entity.

Tested classes:
- app.domain.entities.board.Board
"""

import pytest
from datetime import datetime, UTC
from app.domain.values.name import Name
from app.domain.values.description import Description
from app.domain.values.entity_id import EntityId
from app.domain.collections.column_collection import ColumnCollection
from app.domain.entities.column import Column

TEST_BOARD_ID = EntityId.new()
TEST_BOARD_NAME = Name("Test Board")
TEST_BOARD_DESCRIPTION = Description("This is a test board.")
TEST_CREATED_AT = datetime.now(tz=UTC)
TEST_CREATED_BY = EntityId.new()
TEST_BOARD_COLUMNS = ColumnCollection(
    [Column(id=EntityId.new(), name=Name("Column 1"), description=Description("First test column."), created_by=TEST_CREATED_BY),
    Column(id=EntityId.new(), name=Name("Column 2"), description=Description("Second test column."), created_by=TEST_CREATED_BY)]
)

class TestBoard:
    
    @pytest.fixture()
    def fresh_board(self) -> Board:
        """Create a fresh Board for each test."""
        return Board(
            id=TEST_BOARD_ID, 
            name=TEST_BOARD_NAME, 
            description=TEST_BOARD_DESCRIPTION, 
            created_by=TEST_CREATED_BY
        )
    
    @pytest.fixture
    def rehydrated_board(self) -> Board:
        """Create a Board using the rehydrate method."""
        return Board.rehydrate(
            id=TEST_BOARD_ID, 
            name=TEST_BOARD_NAME, 
            description=TEST_BOARD_DESCRIPTION, 
            created_at=TEST_CREATED_AT, 
            created_by=TEST_CREATED_BY,
            initial_columns=TEST_BOARD_COLUMNS
        )

#region Fresh Board Tests
    def test_initialization(self, fresh_board: Board):
        """Test that Board initializes with correct attributes."""
        assert fresh_board.id == TEST_BOARD_ID
        assert fresh_board.name == TEST_BOARD_NAME
        assert fresh_board.description == TEST_BOARD_DESCRIPTION
        assert fresh_board.created_by == TEST_CREATED_BY
#endregion

#region Rehydrated Board Tests
    def test_rehydration(self, rehydrated_board: Board):
        """Test that Board rehydrates with correct attributes."""
        assert rehydrated_board.id == TEST_BOARD_ID
        assert rehydrated_board.name == TEST_BOARD_NAME
        assert rehydrated_board.description == TEST_BOARD_DESCRIPTION
        assert rehydrated_board.created_at == TEST_CREATED_AT
        assert rehydrated_board.created_by == TEST_CREATED_BY
        assert rehydrated_board._columns == TEST_BOARD_COLUMNS
#regionend
        