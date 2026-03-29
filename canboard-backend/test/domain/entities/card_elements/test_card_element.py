from app.domain.entities.card_elements.card_element import CardElement

"""
Tests for the CardElement domain entity.

Tested classes:
- app.domain.entities.card_element.CardElement
"""

import pytest

from test.utils import make_test_metadata, TEST_NAMES, TEST_CONTENTS

class TestCardElement:

    @pytest.fixture
    def card_element(self) -> CardElement:
        return CardElement(
            make_test_metadata(),
            TEST_NAMES[0],
            TEST_CONTENTS[0]
        )
        
    def test_initialization(self, card_element: CardElement):
        assert card_element.name == TEST_NAMES[0]
        assert card_element.content == TEST_CONTENTS[0]
