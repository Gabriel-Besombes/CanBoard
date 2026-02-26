from app.domain.column import Column

"""
Tests for the Column domain entity.

Tested classes:
- app.domain.column.Column
"""

import pytest
from app.domain.card import Card

TEST_COLUMN_ID = 1
TEST_COLUMN_NAME = "Test Column"
TEST_COLUMN_DESCRIPTION = "This is a test column."
TEST_COLUMN_CARDS = [
    Card(id=1, name="Card 1", description="First test card."),
    Card(id=2, name="Card 2", description="Second test card.")
]

class TestColumn:
    
    @pytest.fixture()
    def column(self) -> Column:
        """Create a fresh Column for each test."""
        return Column(id=TEST_COLUMN_ID, name=TEST_COLUMN_NAME, description=TEST_COLUMN_DESCRIPTION)

    def test_initialization_without_cards(self, column: Column):
        """Test that Column initializes with correct attributes."""
        assert column.id == TEST_COLUMN_ID
        assert column.name == TEST_COLUMN_NAME
        assert column.description == TEST_COLUMN_DESCRIPTION
        assert column.cards == []
        
    def test_initialization_with_cards(self):
        """Test that Column initializes with a list of cards."""
        column = Column(id=TEST_COLUMN_ID, name=TEST_COLUMN_NAME, description=TEST_COLUMN_DESCRIPTION, cards=TEST_COLUMN_CARDS)
        assert column.cards == TEST_COLUMN_CARDS
        
    def test_add_card(self, column: Column):
        """Test that a card can be added to the column."""
        column.add_card(TEST_COLUMN_CARDS[0])
        assert TEST_COLUMN_CARDS[0] in column.cards
    
    def test_remove_card(self, column: Column):
        """Test that a card can be removed from the column."""
        column.add_card(TEST_COLUMN_CARDS[0])
        column.remove_card(TEST_COLUMN_CARDS[0])
        assert TEST_COLUMN_CARDS[0] not in column.cards
        
    def test_remove_nonexistent_card(self, column: Column):
        """Test that removing a card that is not in the column does not raise an error."""
        column.remove_card(TEST_COLUMN_CARDS[0])  # Should not raise an error
        
    def test_add_duplicate_card(self, column: Column):
        """Test that adding the same card multiple times does not create duplicates."""
        column.add_card(TEST_COLUMN_CARDS[0])
        column.add_card(TEST_COLUMN_CARDS[0])  # Adding the same card again
        assert column.cards.count(TEST_COLUMN_CARDS[0]) == 1  # Should only be one instance of the card
        
    def test_card_order(self):
        """Test that cards are stored in the order they were added."""
        column = Column(id=TEST_COLUMN_ID, name=TEST_COLUMN_NAME, description=TEST_COLUMN_DESCRIPTION)
        column.add_card(TEST_COLUMN_CARDS[0])
        column.add_card(TEST_COLUMN_CARDS[1])
        assert column.cards == TEST_COLUMN_CARDS  # Cards should be in the order they were added
        
    def test_move_card_in_column(self):
        """Test that a card can be moved in a column."""
        column = Column(id=TEST_COLUMN_ID, name=TEST_COLUMN_NAME, description=TEST_COLUMN_DESCRIPTION)
        column.add_card(TEST_COLUMN_CARDS[0])
        column.add_card(TEST_COLUMN_CARDS[1])
        column.move_card(TEST_COLUMN_CARDS[0], 1)  # Move the first card to index 1
        assert column.cards == [TEST_COLUMN_CARDS[1], TEST_COLUMN_CARDS[0]]  # Cards should be swapped
        
        column.move_card(TEST_COLUMN_CARDS[0], 0)  # Move the first card back to index 0
        assert column.cards == TEST_COLUMN_CARDS  # Cards should be back in original order