from app.domain.entities.card import Card

"""
Tests for the Card domain entity.

Tested classes:
- app.domain.entities.card.Card
"""

import pytest

from app.domain.collections import CardElementCollection
from app.domain.entities import Card
from app.domain.entities.card_elements import CardElement
from app.domain.errors import AlreadyExistsError, NotFoundError
from test.utils import make_test_metadata, TEST_NAMES, TEST_DESCRIPTIONS, TEST_CONTENTS


class TestCard:

    @pytest.fixture
    def card(self) -> Card:
        return Card(
            make_test_metadata(),
            TEST_NAMES[0],
            TEST_DESCRIPTIONS[0],
        )
        
    def test_initialization_without_elements(self, card: Card):
        assert card.name == TEST_NAMES[0]
        assert card.description == TEST_DESCRIPTIONS[0]
        assert card.elements == ()

    def test_initialization_with_elements(self):
        element = CardElement(
            make_test_metadata(),
            TEST_NAMES[1],
            TEST_CONTENTS[1],
        )
        card = Card(
            make_test_metadata(),
            TEST_NAMES[0],
            TEST_DESCRIPTIONS[0],
            elements=CardElementCollection([element]),
        )

        assert card.elements == (element,)

    def test_append_element(self, card: Card):
        element = CardElement(
            make_test_metadata(),
            TEST_NAMES[1],
            TEST_CONTENTS[1],
        )

        card.append_element(element)
        assert card.elements == (element,)

    def test_append_duplicate_element_raises(self, card: Card):
        element = CardElement(
            make_test_metadata(),
            TEST_NAMES[1],
            TEST_CONTENTS[1],
        )

        card.append_element(element)
        with pytest.raises(AlreadyExistsError):
            card.append_element(element)

    def test_remove_element(self, card: Card):
        element = CardElement(
            make_test_metadata(),
            TEST_NAMES[1],
            TEST_CONTENTS[1],
        )

        card.append_element(element)
        card.remove_element(element)
        assert card.elements == ()

    def test_remove_nonexistent_element_raises(self, card: Card):
        element = CardElement(
            make_test_metadata(),
            TEST_NAMES[1],
            TEST_CONTENTS[1],
        )

        with pytest.raises(NotFoundError):
            card.remove_element(element)

    def test_move_element_by_id(self, card: Card):
        first_element = CardElement(
            make_test_metadata(),
            TEST_NAMES[1],
            TEST_CONTENTS[1],
        )
        second_element = CardElement(
            make_test_metadata(),
            TEST_NAMES[2],
            TEST_CONTENTS[2],
        )

        card.append_element(first_element)
        card.append_element(second_element)
        card.move_element_by_id(first_element.id, 1)

        assert card.elements == (second_element, first_element)

    def test_get_element_by_index(self):
        first_element = CardElement(
            make_test_metadata(),
            TEST_NAMES[1],
            TEST_CONTENTS[1],
        )
        card = Card(
            make_test_metadata(),
            TEST_NAMES[0],
            TEST_DESCRIPTIONS[0],
            elements=CardElementCollection([first_element]),
        )

        assert card.get_element_by_index(0) == first_element

    def test_get_element_by_id(self):
        first_element = CardElement(
            make_test_metadata(),
            TEST_NAMES[1],
            TEST_CONTENTS[1],
        )
        card = Card(
            make_test_metadata(),
            TEST_NAMES[0],
            TEST_DESCRIPTIONS[0],
            elements=CardElementCollection([first_element]),
        )

        assert card.get_element_by_id(first_element.id) == first_element
