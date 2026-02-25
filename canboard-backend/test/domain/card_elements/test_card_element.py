from app.domain.card_elements.card_element import CardElement

"""
Tests for the CardElement domain entity.

Tested classes:
- app.domain.card_element.CardElement
"""

import pytest

class TestElement(CardElement):
    """Empty subclass of CardElement for testing purposes. All testing will be done on this dummy class since CardElement is abstract."""
    
    def __init__(self, id, name, content=None):
        super().__init__(id, name, content)

TEST_CARD_ELEMENT_ID = 1
TEST_CARD_ELEMENT_NAME = "Test Card Element"
TEST_CARD_ELEMENT_CONTENT = "Test Content"

@pytest.mark.tested_classes("CardElement")
class TestCardElement:
    
    @pytest.fixture()
    def test_element(self) -> TestElement:
        """Create a fresh CardElement for each test."""
        return TestElement(id=TEST_CARD_ELEMENT_ID, name=TEST_CARD_ELEMENT_NAME, content=TEST_CARD_ELEMENT_CONTENT)

    def test_initialization(self, test_element: TestElement):
        """Test that CardElement initializes with correct attributes."""
        assert test_element.id == TEST_CARD_ELEMENT_ID
        assert test_element.name == TEST_CARD_ELEMENT_NAME
        assert test_element.content == TEST_CARD_ELEMENT_CONTENT