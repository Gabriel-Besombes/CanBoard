from datetime import datetime, UTC
from uuid import UUID
from app.application.use_cases.metadata_factory import MetaDataFactory
from app.domain.values import EntityId, MetaData, Name, Description

TEST_ENTITY_IDS = [
    UUID("019d3ab9-707e-7404-b81e-a32324308a2b"),
    UUID("019d3ab9-76a4-72b6-9600-11586e61dcce"),
    UUID("019d3ab9-7ca5-7702-a11c-f8df5e3b780e"),
    UUID("019d3ab9-813d-770d-b724-f4a64b864d29"),
    UUID("019d3ab9-9a16-7528-89b4-a92c7941e7ce"),
    UUID("019d3ab9-9f24-7353-84ac-afff2ae956b1"),
    UUID("019d3ab9-a706-754a-9b5b-07cf1fc308c1"),
    UUID("019d3ab9-b724-732b-a656-6881d5aafb1b"),
]
TEST_NAMES = [
    Name("Test Name 1"),
    Name("Test Name 2"),
    Name("Test Name 3"),
    Name("Test Name 4"),
    Name("Test Name 5"),
    Name("Test Name 6"),
    Name("Test Name 7"),
    Name("Test Name 8"),
]
TEST_DESCRIPTIONS = [
    Description("Test Description 1"),
    Description("Test Description 2"),
    Description("Test Description 3"),
    Description("Test Description 4"),
    Description("Test Description 5"),
    Description("Test Description 6"),
    Description("Test Description 7"),
    Description("Test Description 8"),
]
TEST_CONTENTS = [
    "Test Content 1",
    "Test Content 2",
    "Test Content 3",
    "Test Content 4",
    1,
    2,
    3,
    4,
]

def make_test_metadata(
    id : EntityId | None = None, 
    created_at : datetime | None = None, 
    created_by : EntityId | None = None) -> MetaData:
    return MetaDataFactory.rehydrate(
        id=id or EntityId.new(),
        created_at=created_at or datetime.now(tz=UTC),
        created_by=created_by or EntityId.new(),
    )