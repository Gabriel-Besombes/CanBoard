from app.domain.entities.column import Column

"""
Tests for the Column domain entity.

Tested classes:
- app.domain.entities.column.Column
"""

import pytest

from app.domain.collections import CardCollection
from app.domain.entities import Card, Column
from app.domain.entities.column import Column
from app.domain.errors import AlreadyExistsError, InvalidEntityError, NotFoundError
from app.domain.values import EntityId
from test.utils import make_test_metadata, TEST_NAMES, TEST_DESCRIPTIONS


class TestColumn:

    @pytest.fixture
    def column(self) -> Column:
        return Column(
            make_test_metadata(),
            TEST_NAMES[0],
            TEST_DESCRIPTIONS[0],
        )

    def test_initialization_without_cards(self, column: Column):
        assert column.name == TEST_NAMES[0]
        assert column.description == TEST_DESCRIPTIONS[0]
        assert column.cards == ()

    def test_initialization_with_cards(self):
        first_card = Card(
            make_test_metadata(),
            TEST_NAMES[1],
            TEST_DESCRIPTIONS[1],
        )
        second_card = Card(
            make_test_metadata(),
            TEST_NAMES[2],
            TEST_DESCRIPTIONS[2],
        )
        column = Column(
            make_test_metadata(),
            TEST_NAMES[0],
            TEST_DESCRIPTIONS[0],
            CardCollection([first_card, second_card]),
        )

        assert column.cards == (first_card, second_card)

    def test_append_and_remove_card(self, column: Column):
        card = Card(
            make_test_metadata(),
            TEST_NAMES[3],
            TEST_DESCRIPTIONS[3],
        )

        column.append_card(card)
        assert column.cards == (card,)

        column.remove_card(card)
        assert column.cards == ()

    def test_append_duplicate_card_raises(self, column: Column):
        card = Card(
            make_test_metadata(),
            TEST_NAMES[1],
            TEST_DESCRIPTIONS[1],
        )

        column.append_card(card)
        with pytest.raises(AlreadyExistsError):
            column.append_card(card)

    def test_remove_nonexistent_card_raises(self, column: Column):
        card = Card(
            make_test_metadata(),
            TEST_NAMES[1],
            TEST_DESCRIPTIONS[1],
        )

        with pytest.raises(NotFoundError):
            column.remove_card(card)

    def test_insert_card_preserves_order(self, column: Column):
        first_card = Card(
            make_test_metadata(),
            TEST_NAMES[1],
            TEST_DESCRIPTIONS[1],
        )
        second_card = Card(
            make_test_metadata(),
            TEST_NAMES[2],
            TEST_DESCRIPTIONS[2],
        )

        column.append_card(first_card)
        column.insert_card(0, second_card)
        assert column.cards == (second_card, first_card)

    def test_get_card_by_id(self):
        card = Card(
            make_test_metadata(),
            TEST_NAMES[1],
            TEST_DESCRIPTIONS[1],
        )
        column = Column(
            make_test_metadata(),
            TEST_NAMES[0],
            TEST_DESCRIPTIONS[0],
            CardCollection([card]),
        )

        assert column.get_card_by_id(card.id) == card

    def test_get_card_by_id_not_found(self, column: Column):
        with pytest.raises(NotFoundError):
            column.get_card_by_id(EntityId.new())

    def test_move_card_by_id(self):
        first_card = Card(
            make_test_metadata(),
            TEST_NAMES[1],
            TEST_DESCRIPTIONS[1],
        )
        second_card = Card(
            make_test_metadata(),
            TEST_NAMES[2],
            TEST_DESCRIPTIONS[2],
        )
        column = Column(
            make_test_metadata(),
            TEST_NAMES[0],
            TEST_DESCRIPTIONS[0],
            CardCollection([first_card, second_card]),
        )

        column.move_card_by_id(first_card.id, 1)
        assert column.cards == (second_card, first_card)

    def test_invalid_card_type_rejected(self, column: Column):
        with pytest.raises(InvalidEntityError):
            column.append_card("not a card")
