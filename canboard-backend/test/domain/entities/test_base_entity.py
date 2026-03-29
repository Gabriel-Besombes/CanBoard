from app.domain.entities.base_entity import BaseEntity

"""
Tests for the BaseEntity domain entity.

Tested classes:
- app.domain.entities.base_entity.BaseEntity
"""

import pytest

from app.domain.values import MetaData
from app.application.use_cases.metadata_factory import MetaDataFactory
from test.utils import make_test_metadata


class TestBaseEntity:

    @pytest.fixture
    def metadata(self) -> MetaData:
        return make_test_metadata()

    @pytest.fixture
    def base_entity(self, metadata: MetaData) -> BaseEntity:
        return BaseEntity(metadata)

    def test_base_entity_metadata(self, base_entity: BaseEntity, metadata: MetaData):
        assert base_entity.metadata == metadata
        assert base_entity.id == metadata.id
        assert base_entity.created_at == metadata.created_at
        assert base_entity.created_by == metadata.created_by

    def test_base_entity_equality_by_id(self, metadata: MetaData):
        metadata_copy = MetaDataFactory.rehydrate(
            id=metadata.id,
            created_at=metadata.created_at,
            created_by=metadata.created_by,
        )
        entity1 = BaseEntity(metadata)
        entity2 = BaseEntity(metadata_copy)

        assert entity1 == entity2
        assert hash(entity1) == hash(entity2)

    def test_base_entity_not_equal_other_type(self, base_entity: BaseEntity):
        assert base_entity != object()
        assert base_entity.__eq__(object()) is NotImplemented
