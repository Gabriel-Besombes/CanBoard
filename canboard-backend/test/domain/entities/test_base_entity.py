from app.domain.entities.base_entity import BaseEntity

"""
Tests for the BaseEntity domain entity abstract base class.

Tested classes:
- app.domain.entities.base_entity.BaseEntity
"""

import pytest
from pydantic import ValidationError
from app.domain.values.entity_id import EntityId
from datetime import datetime, UTC

TEST_BASE_ENTITY_ID = EntityId.new()
TEST_CREATED_AT = datetime.now(tz=UTC)
TEST_CREATED_BY = EntityId.new()

class TestBaseEntity:

    @pytest.fixture
    def test_entity(self) -> BaseEntity:
        """Create a fresh BaseEntity for each test."""
        return BaseEntity(id=TEST_BASE_ENTITY_ID, created_at=TEST_CREATED_AT, created_by=TEST_CREATED_BY)
    
    def test_entity_initialization(self, test_entity: BaseEntity):
        """Test that BaseEntity initializes with an id."""
        assert test_entity.id == TEST_BASE_ENTITY_ID
            
    def test_entity_defaults(self):
        """Test that BaseEntity fills in default values for optional fields."""
        before = datetime.now(tz=UTC)
        entity = BaseEntity(created_by=TEST_CREATED_BY)
        after = datetime.now(tz=UTC)

        assert isinstance(entity.id, EntityId)
        assert isinstance(entity.created_at, datetime)
        assert before <= entity.created_at <= after
        assert entity.created_at.tzinfo is UTC
        assert entity.created_by == TEST_CREATED_BY

    def test_entity_frozen_fields(self, test_entity: BaseEntity):
        """Test that BaseEntity fields are frozen (read-only)."""
        with pytest.raises(ValidationError):
            test_entity.id = EntityId.new()
        with pytest.raises(ValidationError):
            test_entity.created_at = datetime.now(tz=UTC)
        with pytest.raises(ValidationError):
            test_entity.created_by = EntityId.new()

    def test_entity_error_on_wrong_id_type(self):
        """Test that BaseEntity raises an error when initialized with a non-EntityId id."""
        with pytest.raises(ValidationError):
            BaseEntity(id="not an EntityId")
        with pytest.raises(ValidationError):
            BaseEntity(id=3.14)
            
    def test_entity_equality(self):
        """Test equality of BaseEntity instances."""
        entity1 = BaseEntity(id=TEST_BASE_ENTITY_ID, created_at=TEST_CREATED_AT, created_by=TEST_CREATED_BY)
        entity2 = BaseEntity(id=TEST_BASE_ENTITY_ID, created_at=TEST_CREATED_AT, created_by=TEST_CREATED_BY)
        entity3 = BaseEntity(id=EntityId.new(), created_at=TEST_CREATED_AT, created_by=TEST_CREATED_BY)
        
        assert entity1 == entity2
        assert entity1 != entity3
        assert entity2 != entity3

    def test_entity_eq_with_different_type(self, test_entity: BaseEntity):
        """Test equality behavior when comparing to a different type."""
        assert test_entity.__eq__(object()) is NotImplemented
        assert (test_entity == object()) is False
        
    def test_entity_hashing(self):
        """Test that BaseEntity instances can be hashed."""
        entity1 = BaseEntity(id=TEST_BASE_ENTITY_ID, created_at=TEST_CREATED_AT, created_by=TEST_CREATED_BY)
        entity2 = BaseEntity(id=TEST_BASE_ENTITY_ID, created_at=datetime.now(tz=UTC), created_by=EntityId.new())
        entity3 = BaseEntity(id=EntityId.new(), created_at=datetime.now(tz=UTC), created_by=EntityId.new())
        
        assert hash(entity1) == hash(entity2)
        assert hash(entity1) != hash(entity3)
        assert hash(entity2) != hash(entity3)