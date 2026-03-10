from app.domain.entities.card_elements.text_field import TextField

"""
Tests for the TextField domain entity.

Tested classes:
- app.domain.entities.card_elements.TextField
"""

import pytest
from app.domain.values.entity_id import EntityId

TEST_TEXT_FIELD_ID = EntityId.new()
TEST_TEXT_FIELD_NAME = "Test Text Field"
TEST_TEXT_FIELD_CONTENT = "This is a test text field."

class TestTextField:
    
    @pytest.fixture()
    def text_field(self) -> TextField:
        """Create a fresh TextField for each test."""
        return TextField(id=TEST_TEXT_FIELD_ID, name=TEST_TEXT_FIELD_NAME, content=TEST_TEXT_FIELD_CONTENT)

    def test_initialization(self, text_field: TextField):
        """Test that TextField initializes with correct attributes."""
        assert text_field.id == TEST_TEXT_FIELD_ID
        assert text_field.name == TEST_TEXT_FIELD_NAME
        assert text_field.content == TEST_TEXT_FIELD_CONTENT