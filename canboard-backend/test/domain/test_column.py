from app.domain.column import Column

"""
Tests for the Column domain entity.

Tested classes:
- app.domain.column.Column
"""

import pytest

TEST_COLUMN_ID = 1
TEST_COLUMN_NAME = "Test Column"
TEST_COLUMN_DESCRIPTION = "This is a test column."


@pytest.mark.tested_classes("Column")
class TestColumn:
    
    @pytest.fixture()
    def column(self) -> Column:
        """Create a fresh Column for each test."""
        return Column(id=TEST_COLUMN_ID, name=TEST_COLUMN_NAME, description=TEST_COLUMN_DESCRIPTION)

    def test_initialization(self, column: Column):
        """Test that Column initializes with correct attributes."""
        assert column.id == TEST_COLUMN_ID
        assert column.name == TEST_COLUMN_NAME
        assert column.description == TEST_COLUMN_DESCRIPTION