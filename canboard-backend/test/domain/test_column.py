from app.domain.column import Column

"""
Tests for the Column domain entity.

Tested classes:
- app.domain.column.Column
"""

import pytest
from app.domain.card import Card
from app.domain.values.name import Name
from app.domain.values.description import Description

TEST_COLUMN_ID = 1
TEST_COLUMN_NAME = Name("Test Column")
TEST_COLUMN_DESCRIPTION = Description("This is a test column.")
TEST_COLUMN_CARDS = [
    Card(id=1, name=Name("Card 1"), description=Description("First test card.")),
    Card(id=2, name=Name("Card 2"), description=Description("Second test card."))
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

    def test_move_card_nonexistent(self, column: Column):
        """Test that moving a card that is not in the column raises an error."""
        column.add_card(TEST_COLUMN_CARDS[0])
        with pytest.raises(ValueError):
            column.move_card(TEST_COLUMN_CARDS[1], 0)  # Moving a non-existent card should raise an error

    def test_insert_card_at_beginning(self, column: Column):
        """Test that a card can be inserted at the beginning of the column."""
        column.add_card(TEST_COLUMN_CARDS[1])
        column.insert_card(0, TEST_COLUMN_CARDS[0])
        assert column.cards == TEST_COLUMN_CARDS
        
    def test_insert_card_in_middle(self):
        """Test that a card can be inserted in the middle of the column."""
        column = Column(id=TEST_COLUMN_ID, name=TEST_COLUMN_NAME, description=TEST_COLUMN_DESCRIPTION)
        third_card = Card(id=3, name=Name("Card 3"), description=Description("Third test card."))
        column.add_card(TEST_COLUMN_CARDS[0])
        column.add_card(TEST_COLUMN_CARDS[1])
        column.insert_card(1, third_card)
        assert column.cards == [TEST_COLUMN_CARDS[0], third_card, TEST_COLUMN_CARDS[1]]
        
    def test_insert_card_at_end(self, column: Column):
        """Test that a card can be inserted at the end of the column."""
        column.add_card(TEST_COLUMN_CARDS[0])
        column.insert_card(1, TEST_COLUMN_CARDS[1])
        assert column.cards == TEST_COLUMN_CARDS
        
    def test_insert_card_at_end_empty_column(self, column: Column):
        """Test that a card can be inserted in an empty column."""
        column.insert_card(0, TEST_COLUMN_CARDS[0])
        assert column.cards == [TEST_COLUMN_CARDS[0]]
        
    def test_insert_card_invalid_index_negative(self, column: Column):
        """Test that inserting a card with a negative index raises an error."""
        with pytest.raises(ValueError):
            column.insert_card(-1, TEST_COLUMN_CARDS[0])
            
    def test_insert_card_invalid_index_out_of_bounds(self, column: Column):
        """Test that inserting a card with an index out of bounds raises an error."""
        column.add_card(TEST_COLUMN_CARDS[0])
        with pytest.raises(ValueError):
            column.insert_card(2, TEST_COLUMN_CARDS[1])  # Index 2 is out of bounds for a list with 1 element
            
    def test_insert_card_invalid_type_index(self, column: Column):
        """Test that inserting a card with a non-integer index raises an error."""
        with pytest.raises(ValueError):
            column.insert_card("0", TEST_COLUMN_CARDS[0])
            
    def test_insert_card_invalid_type_card(self, column: Column):
        """Test that inserting a non-Card object raises an error."""
        with pytest.raises(ValueError):
            column.insert_card(0, "not a card")

    def test_name_setter_valid(self, column: Column):
        """Test that the name setter accepts valid Name instances."""
        new_name = Name("Updated Column")
        column.name = new_name
        assert column.name == new_name

    def test_name_setter_invalid_type(self, column: Column):
        """Test that the name setter rejects non-Name objects."""
        with pytest.raises(ValueError):
            column.name = "Invalid Name"

    def test_description_setter_valid(self, column: Column):
        """Test that the description setter accepts valid Description instances."""
        new_description = Description("Updated description.")
        column.description = new_description
        assert column.description == new_description

    def test_description_setter_invalid_type(self, column: Column):
        """Test that the description setter rejects non-Description objects."""
        with pytest.raises(ValueError):
            column.description = "Invalid Description"

    def test_cards_setter_valid_list(self, column: Column):
        """Test that the cards setter accepts valid card lists."""
        column.cards = TEST_COLUMN_CARDS
        assert column.cards == TEST_COLUMN_CARDS

    def test_cards_setter_none(self, column: Column):
        """Test that the cards setter handles None by initializing an empty list."""
        column.cards = None
        assert column.cards == []

    def test_cards_setter_empty_list(self, column: Column):
        """Test that the cards setter handles empty lists properly."""
        column.add_card(TEST_COLUMN_CARDS[0])
        column.cards = []
        assert column.cards == []

    def test_cards_setter_invalid_type_not_list(self, column: Column):
        """Test that the cards setter rejects non-list objects."""
        with pytest.raises(ValueError):
            column.cards = TEST_COLUMN_CARDS[0]  # Passing a single card instead of a list

    def test_cards_setter_invalid_list_contains_non_card(self, column: Column):
        """Test that the cards setter rejects lists containing non-Card objects."""
        with pytest.raises(ValueError):
            column.cards = [TEST_COLUMN_CARDS[0], "not a card", TEST_COLUMN_CARDS[1]]

    def test_cards_property_returns_copy(self, column: Column):
        """Test that the cards property returns a copy, not the original list."""
        column.add_card(TEST_COLUMN_CARDS[0])
        cards_copy = column.cards
        cards_copy.append(TEST_COLUMN_CARDS[1])
        # Original cards list should remain unchanged
        assert len(column.cards) == 1
        assert TEST_COLUMN_CARDS[1] not in column.cards

    def test_repr_method(self, column: Column):
        """Test the string representation of the Column."""
        repr_string = repr(column)
        assert "Column" in repr_string
        assert str(TEST_COLUMN_ID) in repr_string
        assert str(TEST_COLUMN_NAME) in repr_string
        assert str(TEST_COLUMN_DESCRIPTION) in repr_string