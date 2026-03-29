from app.domain.entities.board import Board

"""
Tests for the Board domain entity.

Tested classes:
- app.domain.entities.board.Board
"""

import pytest

from app.domain.values import EntityId
from app.domain.errors import NotFoundError
from app.domain.entities import Column, Card
from app.domain.collections import ColumnCollection
from test.utils import make_test_metadata, TEST_NAMES, TEST_DESCRIPTIONS



class TestBoard:

    @pytest.fixture
    def board(self) -> Board:
        return Board(
            make_test_metadata(),
            TEST_NAMES[0],
            TEST_DESCRIPTIONS[0],
        )

    def test_initialization_without_columns(self, board: Board):

        assert board.name == TEST_NAMES[0]
        assert board.description == TEST_DESCRIPTIONS[0]
        assert board.columns == ()

    def test_initialization_with_columns(self):
        first_column = Column(
            make_test_metadata(),
            TEST_NAMES[1],
            TEST_DESCRIPTIONS[1],
        )
        board = Board(
            make_test_metadata(),
            TEST_NAMES[0],
            TEST_DESCRIPTIONS[0],
            ColumnCollection([first_column]),
        )

        assert board.columns == (first_column,)
        assert board.get_column_by_id(first_column.id) is first_column
        assert board.get_column_by_index(0) is first_column

    def test_append_and_remove_column(self, board: Board):

        column = Column(
            make_test_metadata(),
            TEST_NAMES[1],
            TEST_DESCRIPTIONS[1],
        )

        board.append_column(column)
        assert board.columns == (column,)

        board.remove_column_by_id(column.id)
        assert board.columns == ()

    def test_move_columns(self):
        first_column = Column(
            make_test_metadata(),
            TEST_NAMES[1],
            TEST_DESCRIPTIONS[1],
        )
        second_column = Column(
            make_test_metadata(),
            TEST_NAMES[2],
            TEST_DESCRIPTIONS[2],
        )
        board = Board(
            make_test_metadata(),
            TEST_NAMES[0],
            TEST_DESCRIPTIONS[0],
            ColumnCollection([first_column, second_column]),
        )

        board.move_column_by_id(second_column.id, 0)
        assert board.columns == (second_column, first_column)

    def test_append_and_move_card_between_columns(self):
        first_column = Column(
            make_test_metadata(),
            TEST_NAMES[1],
            TEST_DESCRIPTIONS[1],
        )
        second_column = Column(
            make_test_metadata(),
            TEST_NAMES[2],
            TEST_DESCRIPTIONS[2],
        )
        board = Board(
            make_test_metadata(),
            TEST_NAMES[0],
            TEST_DESCRIPTIONS[0],
            ColumnCollection([first_column, second_column]),
        )

        card = Card(
            make_test_metadata(),
            TEST_NAMES[3],
            TEST_DESCRIPTIONS[3],
        )

        board.append_card(card, first_column.id)
        assert first_column.cards == (card,)

        board.move_card_by_id(card.id, first_column.id, second_column.id)
        assert first_column.cards == ()
        assert second_column.cards == (card,)
        assert board.get_card_by_id(card.id) is card

    def test_get_card_by_id_raises_not_found_for_missing_card(self, board: Board):
        with pytest.raises(NotFoundError):
            board.get_card_by_id(EntityId.new())
        