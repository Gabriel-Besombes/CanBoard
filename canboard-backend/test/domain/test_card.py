from app.domain.card import Card

"""
Tests for the Card domain entity.

Tested classes:
- app.domain.card.Card
"""

import pytest

TEST_CARD_ID = 1
TEST_CARD_NAME = "Test Card"
TEST_CARD_DESCRIPTION = "This is a test card."


@pytest.mark.tested_classes("Card")
class TestCard:
    
    @pytest.fixture()
    def card(self) -> Card:
        """Create a fresh Card for each test."""
        return Card(id=TEST_CARD_ID, name=TEST_CARD_NAME, description=TEST_CARD_DESCRIPTION)

    def test_initialization(self, card: Card):
        """Test that Card initializes with correct attributes."""
        assert card.id == TEST_CARD_ID
        assert card.name == TEST_CARD_NAME
        assert card.description == TEST_CARD_DESCRIPTION