from app.domain.base_entity import BaseEntity

"""
Tests for the BaseEntity domain entity.

Tested classes:
- app.domain.base_entity.BaseEntity
"""

import pytest

TEST_BASE_ENTITY_ID = 1

@pytest.mark.tested_classes("BaseEntity")
class TestBaseEntity:

    @pytest.fixture
    def base_entity(self) -> BaseEntity:
        """Create a fresh BaseEntity for each test."""
        return BaseEntity(id=TEST_BASE_ENTITY_ID)
    
    def test_base_entity_initialization(self, base_entity: BaseEntity):
        """Test that BaseEntity initializes with an id."""
        assert base_entity.id == TEST_BASE_ENTITY_ID
    
    def test_base_entity_with_different_ids(self):
        """Test BaseEntity with various id values."""
        for test_id in [0, 1, 100, 999999]:
            entity = BaseEntity(id=test_id)
            assert entity.id == test_id