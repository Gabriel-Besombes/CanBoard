from app.domain.entities.card_elements.card_element import CardElement

"""
Tests for the CardElement domain entity.

Tested classes:
- app.domain.entities.card_element.CardElement
"""

import pytest
from datetime import datetime, UTC
from app.domain.values.name import Name
from app.domain.values.entity_id import EntityId

TEST_CARD_ELEMENT_ID = EntityId.new()
TEST_CARD_ELEMENT_NAME = Name("Test Card Element")
TEST_CARD_ELEMENT_CONTENT = "Test Content"
TEST_CREATED_AT = datetime.now(tz=UTC)
TEST_CREATED_BY = EntityId.new()

class TestCardElement:
    
    @pytest.fixture()
    def test_element(self) -> CardElement:
        """Create a fresh CardElement for each test."""
        return CardElement(id=TEST_CARD_ELEMENT_ID, name=TEST_CARD_ELEMENT_NAME, content=TEST_CARD_ELEMENT_CONTENT, created_at=TEST_CREATED_AT, created_by=TEST_CREATED_BY)

    def test_initialization(self, test_element: CardElement):
        """Test that CardElement initializes with correct attributes."""
        assert test_element.id == TEST_CARD_ELEMENT_ID
        assert test_element.name == TEST_CARD_ELEMENT_NAME
        assert test_element.content == TEST_CARD_ELEMENT_CONTENT
        assert test_element.created_at == TEST_CREATED_AT
        assert test_element.created_by == TEST_CREATED_BY