from app.domain.entities.card import Card

"""
Tests for the Card domain entity.

Tested classes:
- app.domain.entities.card.Card
"""

import pytest
from app.domain.entities.card_elements.card_element import CardElement
from app.domain.values.entity_id import EntityId

TEST_CARD_ID = EntityId.new()
TEST_CARD_NAME = "Test Card"
TEST_CARD_DESCRIPTION = "This is a test card."

class TestCardElement(CardElement):
    """Empty subclass of CardElement for testing purposes."""
    
    def __init__(self, id, name, content=None):
        super().__init__(id, name, content)

TEST_CARD_ELEMENTS = [
    TestCardElement(id=EntityId.new(), name="Element 1"),
    TestCardElement(id=EntityId.new(), name="Element 2")
]

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
        
    def test_initialization_with_elements(self):
        """Test that Card initializes with a list of card elements."""
        card = Card(id=TEST_CARD_ID, name=TEST_CARD_NAME, description=TEST_CARD_DESCRIPTION, elements=TEST_CARD_ELEMENTS)
        assert card.elements == TEST_CARD_ELEMENTS
    
    def test_add_element(self, card: Card):
        """Test that a card element can be added to the card."""
        card.add_element(TEST_CARD_ELEMENTS[0])
        assert TEST_CARD_ELEMENTS[0] in card.elements
    
    def test_remove_element(self, card: Card):
        """Test that a card element can be removed from the card."""
        card.add_element(TEST_CARD_ELEMENTS[0])
        card.remove_element(TEST_CARD_ELEMENTS[0])
        assert TEST_CARD_ELEMENTS[0] not in card.elements
    
    def test_remove_nonexistent_element(self, card: Card):
        """Test that removing a card element that is not in the card does not raise an error."""
        card.remove_element(TEST_CARD_ELEMENTS[0])  # Should not raise an error
    
    def test_add_duplicate_element(self, card: Card):
        """Test that adding the same card element multiple times does not create duplicates."""
        card.add_element(TEST_CARD_ELEMENTS[0])
        card.add_element(TEST_CARD_ELEMENTS[0])  # Adding the same element again
        assert card.elements.count(TEST_CARD_ELEMENTS[0]) == 1  # Should only be one instance of the element
        
    def test_element_order(self):
        """Test that card elements are stored in the order they were added."""
        card = Card(id=TEST_CARD_ID, name=TEST_CARD_NAME, description=TEST_CARD_DESCRIPTION)
        card.add_element(TEST_CARD_ELEMENTS[0])
        card.add_element(TEST_CARD_ELEMENTS[1])
        assert card.elements == TEST_CARD_ELEMENTS  # Should be in the order they were added
    
    def test_move_element_in_card(self):
        """Test that a card element can be moved in a card."""
        card = Card(id=TEST_CARD_ID, name=TEST_CARD_NAME, description=TEST_CARD_DESCRIPTION)
        card.add_element(TEST_CARD_ELEMENTS[0])
        card.add_element(TEST_CARD_ELEMENTS[1])
        card.move_element(TEST_CARD_ELEMENTS[0], 1)  # Move first element to index 1
        assert card.elements == [TEST_CARD_ELEMENTS[1], TEST_CARD_ELEMENTS[0]]  # Elements should be swapped
        
        card.move_element(TEST_CARD_ELEMENTS[0], 0)  # Move first element back to index 0
        assert card.elements == TEST_CARD_ELEMENTS  # Elements should be back in original order