from app.domain.values.name import Name

"""
Tests for the Name domain value object.

Tested classes:
- app.domain.values.name.Name
"""

import pytest

from dataclasses import FrozenInstanceError

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

    def test_name_is_immutable(self):
        name = Name("Initial")
        with pytest.raises(FrozenInstanceError):
            name.value = "Updated name"

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
        assert name is not None