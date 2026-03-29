from app.domain.entities.column import Column

"""
Tests for the Column domain entity.

Tested classes:
- app.domain.entities.column.Column
"""

import pytest
from datetime import datetime, UTC
from app.domain.values.entity_id import EntityId
from app.domain.entities.card import Card
from app.domain.values.name import Name
from app.domain.values.description import Description
from app.domain.collections.card_collection import CardCollection

TEST_COLUMN_ID = EntityId.new()
TEST_COLUMN_NAME = Name("Test Column")
TEST_COLUMN_DESCRIPTION = Description("This is a test column.")
TEST_CREATED_AT = datetime.now(tz=UTC)
TEST_CREATED_BY = EntityId.new()
TEST_COLUMN_CARDS = CardCollection([
    Card(id=EntityId.new(), name=Name("Card 1"), description=Description("First test card."), created_by=TEST_CREATED_BY),
    Card(id=EntityId.new(), name=Name("Card 2"), description=Description("Second test card."), created_by=TEST_CREATED_BY)
])

class TestColumn:
    
    @pytest.fixture()
    def fresh_column(self) -> Column:
        """Create a fresh Column for each test."""
        return Column(id=TEST_COLUMN_ID, name=TEST_COLUMN_NAME, description=TEST_COLUMN_DESCRIPTION, created_by=TEST_CREATED_BY)

#region Fresh Column Tests
    def test_initialization_without_cards(self, fresh_column: Column):
        """Test that Column initializes with correct attributes."""
        assert fresh_column.id == TEST_COLUMN_ID
        assert fresh_column.name == TEST_COLUMN_NAME
        assert fresh_column.description == TEST_COLUMN_DESCRIPTION
        assert fresh_column.created_by == TEST_CREATED_BY
#regionend
        
#region Rehydrated Column Tests
    def test_initialization_with_cards(self, fresh_column: Column):
        """Test that Column initializes with a list of cards."""
        assert fresh_column.cards == TEST_COLUMN_CARDS
        
    def test_add_card(self, fresh_column: Column):
        """Test that a card can be added to the column."""
        fresh_column.add_card(TEST_COLUMN_CARDS[0])
        assert TEST_COLUMN_CARDS[0] in fresh_column.cards
    
    def test_remove_card(self, fresh_column: Column):
        """Test that a card can be removed from the column."""
        fresh_column.add_card(TEST_COLUMN_CARDS[0])
        fresh_column.remove_card(TEST_COLUMN_CARDS[0])
        assert TEST_COLUMN_CARDS[0] not in fresh_column.cards
        
    def test_remove_nonexistent_card(self, fresh_column: Column):
        """Test that removing a card that is not in the column does not raise an error."""
        fresh_column.remove_card(TEST_COLUMN_CARDS[0])  # Should not raise an error
        
    def test_add_duplicate_card(self, fresh_column: Column):
        """Test that adding the same card multiple times does not create duplicates."""
        fresh_column.add_card(TEST_COLUMN_CARDS[0])
        fresh_column.add_card(TEST_COLUMN_CARDS[0])  # Adding the same card again
        assert fresh_column.cards.count(TEST_COLUMN_CARDS[0]) == 1  # Should only be one instance of the card
        
    def test_card_order(self, fresh_column: Column):
        """Test that cards are stored in the order they were added."""
        fresh_column.add_card(TEST_COLUMN_CARDS[0])
        fresh_column.add_card(TEST_COLUMN_CARDS[1])
        assert fresh_column.cards == TEST_COLUMN_CARDS  # Cards should be in the order they were added
        
    def test_move_card_in_column(self, fresh_column: Column):
        """Test that a card can be moved in a column."""
        fresh_column.add_card(TEST_COLUMN_CARDS[0])
        fresh_column.add_card(TEST_COLUMN_CARDS[1])
        fresh_column.move_card(TEST_COLUMN_CARDS[0], 1)  # Move the first card to index 1
        assert fresh_column.cards == [TEST_COLUMN_CARDS[1], TEST_COLUMN_CARDS[0]]  # Cards should be swapped
        
        fresh_column.move_card(TEST_COLUMN_CARDS[0], 0)  # Move the first card back to index 0
        assert fresh_column.cards == TEST_COLUMN_CARDS  # Cards should be back in original order

    def test_move_card_nonexistent(self, fresh_column: Column):
        """Test that moving a card that is not in the column raises an error."""
        fresh_column.add_card(TEST_COLUMN_CARDS[0])
        with pytest.raises(ValueError):
            fresh_column.move_card(TEST_COLUMN_CARDS[1], 0)  # Moving a non-existent card should raise an error

    def test_get_card_by_id_success(self, fresh_column: Column):
        """Ensure get_card_by_id returns the correct card when present."""
        # add cards and verify lookups
        fresh_column.add_card(TEST_COLUMN_CARDS[0])
        fresh_column.add_card(TEST_COLUMN_CARDS[1])
        assert fresh_column.get_card_by_id(1) == TEST_COLUMN_CARDS[0]
        assert fresh_column.get_card_by_id(2) == TEST_COLUMN_CARDS[1]

    def test_get_card_by_id_not_found(self, fresh_column: Column):
        """get_card_by_id should raise ValueError if card id is missing."""
        fresh_column.add_card(TEST_COLUMN_CARDS[0])
        with pytest.raises(ValueError):
            fresh_column.get_card_by_id(99)

    def test_insert_card_at_beginning(self, fresh_column: Column):
        """Test that a card can be inserted at the beginning of the column."""
        fresh_column.add_card(TEST_COLUMN_CARDS[1])
        fresh_column.insert_card(0, TEST_COLUMN_CARDS[0])
        assert fresh_column.cards == TEST_COLUMN_CARDS
        
    def test_insert_card_in_middle(self, fresh_column: Column):
        """Test that a card can be inserted in the middle of the column."""
        third_card = Card(id=3, name=Name("Card 3"), description=Description("Third test card."))
        fresh_column.add_card(TEST_COLUMN_CARDS[0])
        fresh_column.add_card(TEST_COLUMN_CARDS[1])
        fresh_column.insert_card(1, third_card)
        assert fresh_column.cards == [TEST_COLUMN_CARDS[0], third_card, TEST_COLUMN_CARDS[1]]
        
    def test_insert_card_at_end(self, fresh_column: Column):
        """Test that a card can be inserted at the end of the column."""
        fresh_column.add_card(TEST_COLUMN_CARDS[0])
        fresh_column.insert_card(1, TEST_COLUMN_CARDS[1])
        assert fresh_column.cards == TEST_COLUMN_CARDS
        
    def test_insert_card_at_end_empty_column(self, fresh_column: Column):
        """Test that a card can be inserted in an empty column."""
        fresh_column.insert_card(0, TEST_COLUMN_CARDS[0])
        assert fresh_column.cards == [TEST_COLUMN_CARDS[0]]
        
    def test_insert_card_invalid_index_negative(self, fresh_column: Column):
        """Test that inserting a card with a negative index raises an error."""
        with pytest.raises(ValueError):
            fresh_column.insert_card(-1, TEST_COLUMN_CARDS[0])
            
    def test_insert_card_invalid_index_out_of_bounds(self, fresh_column: Column):
        """Test that inserting a card with an index out of bounds raises an error."""
        fresh_column.add_card(TEST_COLUMN_CARDS[0])
        with pytest.raises(ValueError):
            fresh_column.insert_card(2, TEST_COLUMN_CARDS[1])  # Index 2 is out of bounds for a list with 1 element
            
    def test_insert_card_invalid_type_index(self, fresh_column: Column):
        """Test that inserting a card with a non-integer index raises an error."""
        with pytest.raises(ValueError):
            fresh_column.insert_card("0", TEST_COLUMN_CARDS[0])
            
    def test_insert_card_invalid_type_card(self, fresh_column: Column):
        """Test that inserting a non-Card object raises an error."""
        with pytest.raises(ValueError):
            fresh_column.insert_card(0, "not a card")

    def test_name_setter_valid(self, fresh_column: Column):
        """Test that the name setter accepts valid Name instances."""
        new_name = Name("Updated Column")
        fresh_column.name = new_name
        assert fresh_column.name == new_name

    def test_name_setter_invalid_type(self, fresh_column: Column):
        """Test that the name setter rejects non-Name objects."""
        with pytest.raises(ValueError):
            fresh_column.name = "Invalid Name"

    def test_description_setter_valid(self, fresh_column: Column):
        """Test that the description setter accepts valid Description instances."""
        new_description = Description("Updated description.")
        fresh_column.description = new_description
        assert fresh_column.description == new_description

    def test_description_setter_invalid_type(self, fresh_column: Column):
        """Test that the description setter rejects non-Description objects."""
        with pytest.raises(ValueError):
            fresh_column.description = "Invalid Description"

    def test_cards_setter_valid_list(self, fresh_column: Column):
        """Test that the cards setter accepts valid card lists."""
        fresh_column.cards = TEST_COLUMN_CARDS
        assert fresh_column.cards == TEST_COLUMN_CARDS

    def test_cards_setter_none(self, fresh_column: Column):
        """Test that the cards setter handles None by initializing an empty list."""
        fresh_column.cards = None
        assert fresh_column.cards == []

    def test_cards_setter_empty_list(self, fresh_column: Column):
        """Test that the cards setter handles empty lists properly."""
        fresh_column.add_card(TEST_COLUMN_CARDS[0])
        fresh_column.cards = []
        assert fresh_column.cards == []

    def test_cards_setter_invalid_type_not_list(self, fresh_column: Column):
        """Test that the cards setter rejects non-list objects."""
        with pytest.raises(ValueError):
            fresh_column.cards = TEST_COLUMN_CARDS[0]  # Passing a single card instead of a list

    def test_cards_setter_invalid_list_contains_non_card(self, fresh_column: Column):
        """Test that the cards setter rejects lists containing non-Card objects."""
        with pytest.raises(ValueError):
            fresh_column.cards = [TEST_COLUMN_CARDS[0], "not a card", TEST_COLUMN_CARDS[1]]

    def test_cards_property_returns_copy(self, fresh_column: Column):
        """Test that the cards property returns a copy, not the original list."""
        fresh_column.add_card(TEST_COLUMN_CARDS[0])
        cards_copy = fresh_column.cards
        cards_copy.append(TEST_COLUMN_CARDS[1])
        # Original cards list should remain unchanged
        assert len(fresh_column.cards) == 1
        assert TEST_COLUMN_CARDS[1] not in fresh_column.cards

    def test_repr_method(self, fresh_column: Column):
        """Test the string representation of the Column."""
        repr_string = repr(fresh_column)
        assert "Column" in repr_string
        assert str(TEST_COLUMN_ID) in repr_string
        assert str(TEST_COLUMN_NAME) in repr_string
        assert str(TEST_COLUMN_DESCRIPTION) in repr_string