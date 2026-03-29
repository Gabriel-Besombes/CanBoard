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
    def fresh_entity(self) -> BaseEntity:
        """Create a fresh BaseEntity for each test."""
        return BaseEntity(id=TEST_BASE_ENTITY_ID, created_by=TEST_CREATED_BY)
    
    @pytest.fixture
    def rehydrated_entity(self) -> BaseEntity:
        """Create a BaseEntity using the rehydrate method."""
        return BaseEntity.rehydrate(id=TEST_BASE_ENTITY_ID, created_at=TEST_CREATED_AT, created_by=TEST_CREATED_BY)

#region Fresh Entity Tests
    def test_entity_initialization(self, fresh_entity: BaseEntity):
        """Test that BaseEntity initializes with an id."""
        assert fresh_entity.id == TEST_BASE_ENTITY_ID
        assert isinstance(fresh_entity.created_at, datetime)
        assert fresh_entity.created_at.tzinfo is UTC
        assert fresh_entity.created_by == TEST_CREATED_BY
    
    def test_entity_initialization_fails_with_existing_created_at(self):
        """Test that BaseEntity initialized with an existing created_at return an error."""
        with pytest.raises(ValueError):
            BaseEntity(id=TEST_BASE_ENTITY_ID, created_at=TEST_CREATED_AT, created_by=TEST_CREATED_BY)

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

    def test_entity_frozen_fields(self, fresh_entity: BaseEntity):
        """Test that BaseEntity fields are frozen (read-only)."""
        with pytest.raises(ValidationError):
            fresh_entity.id = EntityId.new()
        with pytest.raises(ValidationError):
            fresh_entity.created_at = datetime.now(tz=UTC)
        with pytest.raises(ValidationError):
            fresh_entity.created_by = EntityId.new()

    def test_entity_error_on_wrong_id_type(self):
        """Test that BaseEntity raises an error when initialized with a non-EntityId id."""
        with pytest.raises(ValidationError):
            BaseEntity(id="not an EntityId")
        with pytest.raises(ValidationError):
            BaseEntity(id=3.14)

    def test_entity_eq_with_different_type(self, fresh_entity: BaseEntity):
        """Test equality behavior when comparing to a different type."""
        assert fresh_entity.__eq__(object()) is NotImplemented
        assert (fresh_entity == object()) is False
#endregion

#region Rehydrated Entity Tests
    def test_rehydrated_entity_initialization(self, rehydrated_entity: BaseEntity):
        """Test that rehydrated BaseEntity initializes with correct attributes."""
        assert rehydrated_entity.id == TEST_BASE_ENTITY_ID
        assert rehydrated_entity.created_at == TEST_CREATED_AT
        assert rehydrated_entity.created_by == TEST_CREATED_BY
            
    def test_entity_equality(self, rehydrated_entity: BaseEntity):
        """Test equality of BaseEntity instances."""
        entity2 = BaseEntity.rehydrate(id=TEST_BASE_ENTITY_ID, created_at=TEST_CREATED_AT, created_by=TEST_CREATED_BY)
        entity3 = BaseEntity.rehydrate(id=EntityId.new(), created_at=TEST_CREATED_AT, created_by=TEST_CREATED_BY)
        
        assert rehydrated_entity == entity2
        assert rehydrated_entity != entity3
        assert entity2 != entity3
        
    def test_entity_hashing(self, rehydrated_entity: BaseEntity):
        """Test that BaseEntity instances can be hashed."""
        entity2 = BaseEntity.rehydrate(id=TEST_BASE_ENTITY_ID, created_at=datetime.now(tz=UTC), created_by=EntityId.new())
        entity3 = BaseEntity.rehydrate(id=EntityId.new(), created_at=datetime.now(tz=UTC), created_by=EntityId.new())
        
        assert hash(rehydrated_entity) == hash(entity2)
        assert hash(rehydrated_entity) != hash(entity3)
        assert hash(entity2) != hash(entity3)
#endregion