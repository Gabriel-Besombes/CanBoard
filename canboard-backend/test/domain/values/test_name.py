from app.domain.values.name import Name

"""
Tests for the Name domain value object.

Tested classes:
- app.domain.values.name.Name
"""

import pytest

class TestName:
    def test_init_with_valid_name(self):
        name = Name("Valid name")
        assert name.value == "Valid name"

    def test_init_with_empty_string_raises_error(self):
        with pytest.raises(ValueError, match="Name cannot be empty"):
            Name("")

    def test_init_with_whitespace_only_raises_error(self):
        with pytest.raises(ValueError, match="Name cannot be empty"):
            Name("   ")

    def test_value_setter_with_valid_value(self):
        name = Name("Initial")
        name.value = "Updated name"
        assert name.value == "Updated name"

    def test_value_setter_with_empty_string_raises_error(self):
        name = Name("Initial")
        with pytest.raises(ValueError, match="Name cannot be empty"):
            name.value = ""

    def test_value_setter_with_whitespace_only_raises_error(self):
        name = Name("Initial")
        with pytest.raises(ValueError, match="Name cannot be empty"):
            name.value = "   "

    def test_equality_with_same_value(self):
        name1 = Name("Same name")
        name2 = Name("Same name")
        assert name1 == name2

    def test_equality_with_different_value(self):
        name1 = Name("Name 1")
        name2 = Name("Name 2")
        assert name1 != name2

    def test_equality_with_non_name_object(self):
        name = Name("Test")
        assert name != "Test"
        assert name != 123
        assert name != None