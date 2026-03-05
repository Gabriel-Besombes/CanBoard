from app.domain.base_entity import BaseEntity

"""
Tests for the BaseEntity domain entity abstract base class.

Tested classes:
- app.domain.base_entity.BaseEntity
"""

import pytest
from app.domain.values.entity_id import EntityId

class TestEntity(BaseEntity):
    """Empty subclass of BaseEntity for testing purposes. All testing will be done on this dummy class since BaseEntity is abstract."""
    
    def __init__(self, id):
        super().__init__(id)

TEST_BASE_ENTITY_ID = EntityId.new()

class TestBaseEntity:

    @pytest.fixture
    def test_entity(self) -> TestEntity:
        """Create a fresh TestEntity for each test."""
        return TestEntity(id=TEST_BASE_ENTITY_ID)
    
    def test_entity_initialization(self, test_entity: TestEntity):
        """Test that TestEntity initializes with an id."""
        assert test_entity.id == TEST_BASE_ENTITY_ID
            
    def test_entity_error_on_non_integer_id(self):
        """Test that TestEntity raises an error when initialized with a non-integer id."""
        with pytest.raises(TypeError):
            TestEntity(id="not an integer")
        with pytest.raises(TypeError):
            TestEntity(id=3.14)
            
    def test_entity_equality(self):
        """Test equality of TestEntity instances."""
        entity1 = TestEntity(id=TEST_BASE_ENTITY_ID)
        entity2 = TestEntity(id=TEST_BASE_ENTITY_ID)
        entity3 = TestEntity(id=EntityId.new())
        
        assert entity1 == entity2
        assert entity1 != entity3
        assert entity2 != entity3
        
    def test_entity_hashing(self):
        """Test that TestEntity instances can be hashed."""
        entity1 = TestEntity(id=TEST_BASE_ENTITY_ID)
        entity2 = TestEntity(id=TEST_BASE_ENTITY_ID)
        entity3 = TestEntity(id=EntityId.new())
        
        assert hash(entity1) == hash(entity2)
        assert hash(entity1) != hash(entity3)
        assert hash(entity2) != hash(entity3)
        
    def test_entity_repr(self, test_entity: TestEntity):
        """Test the string representation of TestEntity."""
        expected_repr = f"TestEntity(id={TEST_BASE_ENTITY_ID})"
        assert repr(test_entity) == expected_repr