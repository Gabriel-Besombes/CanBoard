from app.domain.values.description import Description

"""
Tests for the Description domain value object.

Tested classes:
- app.domain.values.description.Description
"""

import pytest

class TestDescription:
    def test_init_with_valid_description(self):
        description = Description("Valid description")
        assert description.value == "Valid description"

    def test_init_with_empty_string_raises_error(self):
        with pytest.raises(ValueError, match="Description cannot be empty"):
            Description("")

    def test_init_with_whitespace_only_raises_error(self):
        with pytest.raises(ValueError, match="Description cannot be empty"):
            Description("   ")

    def test_value_setter_with_valid_value(self):
        description = Description("Initial")
        description.value = "Updated description"
        assert description.value == "Updated description"

    def test_value_setter_with_empty_string_raises_error(self):
        description = Description("Initial")
        with pytest.raises(ValueError, match="Description cannot be empty"):
            description.value = ""

    def test_value_setter_with_whitespace_only_raises_error(self):
        description = Description("Initial")
        with pytest.raises(ValueError, match="Description cannot be empty"):
            description.value = "   "

    def test_equality_with_same_value(self):
        desc1 = Description("Same description")
        desc2 = Description("Same description")
        assert desc1 == desc2

    def test_equality_with_different_value(self):
        desc1 = Description("Description 1")
        desc2 = Description("Description 2")
        assert desc1 != desc2

    def test_equality_with_non_description_object(self):
        description = Description("Test")
        assert description != "Test"
        assert description != 123
        assert description != None