from app.domain.card_elements.card_element import CardElement

"""
Tests for the CardElement domain entity.

Tested classes:
- app.domain.card_element.CardElement
"""

import pytest

TEST_CARD_ELEMENT_ID = 1
TEST_CARD_ELEMENT_NAME = "Test Card Element"
TEST_CARD_ELEMENT_DESCRIPTION = "This is a test card element."


@pytest.mark.tested_classes("CardElement")
class TestCardElement:
    
    @pytest.fixture()
    def card_element(self) -> CardElement:
        """Create a fresh CardElement for each test."""
        return CardElement(id=TEST_CARD_ELEMENT_ID, name=TEST_CARD_ELEMENT_NAME, description=TEST_CARD_ELEMENT_DESCRIPTION)

    def test_initialization(self, card_element: CardElement):
        """Test that CardElement initializes with correct attributes."""
        assert card_element.id == TEST_CARD_ELEMENT_ID
        assert card_element.name == TEST_CARD_ELEMENT_NAME
        assert card_element.description == TEST_CARD_ELEMENT_DESCRIPTION