from app.domain.board import Board

"""
Tests for the Board domain entity.

Tested classes:
- app.domain.board.Board
"""

import pytest

TEST_BOARD_ID = 1
TEST_BOARD_NAME = "Test Board"
TEST_BOARD_DESCRIPTION = "This is a test board."


@pytest.mark.tested_classes("Board")
class TestBoard:
    
    @pytest.fixture()
    def board(self) -> Board:
        """Create a fresh Board for each test."""
        return Board(id=TEST_BOARD_ID, name=TEST_BOARD_NAME, description=TEST_BOARD_DESCRIPTION)

    def test_initialization(self, board: Board):
        """Test that Board initializes with correct attributes."""
        assert board.id == TEST_BOARD_ID
        assert board.name == TEST_BOARD_NAME
        assert board.description == TEST_BOARD_DESCRIPTION