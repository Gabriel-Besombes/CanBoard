from app.domain.values.entity_id import EntityId

"""
Tests for the EntityId domain value object.

Tested classes:
- app.domain.values.entity_id.EntityId
"""

from uuid import UUID, uuid7, uuid6
import pytest


class TestEntityId:
    def test_init_with_valid_uuidv7(self):
        """Test that EntityId initializes with a valid UUIDv7 works."""
        uuid_v7 = uuid7()
        entity_id = EntityId(uuid_v7)
        assert entity_id.value == uuid_v7

    def test_init_with_invalid_uuid_version_raises_error(self):
        """Test that EntityId raises an error when initialized with a non-UUIDv7."""
        uuid_v6 = uuid6()  # Using uuidv6 as an example of a non-UUIDv7
        with pytest.raises(ValueError, match="Must be UUIDv7"):
            EntityId(uuid_v6)

    def test_new_creates_valid_uuidv7(self):
        """Test that EntityId.new() creates a valid UUIDv7."""
        entity_id = EntityId.new()
        assert isinstance(entity_id.value, UUID)
        assert entity_id.value.version == 7

    def test_new_creates_unique_ids(self):
        """Test that EntityId.new() creates unique IDs."""
        entity_id_1 = EntityId.new()
        entity_id_2 = EntityId.new()
        assert entity_id_1.value != entity_id_2.value

    def test_equality_with_same_value(self):
        """Test equality of EntityId instances with the same value."""
        uuid_v7 = uuid7()
        entity_id_1 = EntityId(uuid_v7)
        entity_id_2 = EntityId(uuid_v7)
        assert entity_id_1 == entity_id_2

    def test_equality_with_different_value(self):
        """Test inequality of EntityId instances with different values."""
        entity_id_1 = EntityId.new()
        entity_id_2 = EntityId.new()
        assert entity_id_1 != entity_id_2

    def test_equality_with_non_entity_id_object(self):
        """Test that EntityId is not equal to non-EntityId objects."""
        entity_id = EntityId.new()
        assert entity_id != entity_id.value
        assert entity_id != "not an entity id"
        assert entity_id != 123
        assert entity_id != None

    def test_entity_id_is_frozen(self):
        """Test that EntityId is immutable (frozen dataclass)."""
        entity_id = EntityId.new()
        with pytest.raises(AttributeError):
            entity_id.value = uuid7()

    def test_entity_id_is_hashable(self):
        """Test that EntityId instances can be hashed."""
        entity_id_1 = EntityId.new()
        entity_id_2 = EntityId.new()
        uuid_v7 = uuid7()
        entity_id_3 = EntityId(uuid_v7)
        entity_id_4 = EntityId(uuid_v7)
        
        assert hash(entity_id_1) != hash(entity_id_2)
        assert hash(entity_id_3) == hash(entity_id_4)