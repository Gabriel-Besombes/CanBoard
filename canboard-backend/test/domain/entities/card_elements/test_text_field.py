from app.domain.entities.card_elements.text_field import TextField

"""
Tests for the TextField domain entity.

Tested classes:
- app.domain.entities.card_elements.TextField
"""

import pytest

from test.utils import make_test_metadata, TEST_NAMES, TEST_CONTENTS
from app.domain.errors import DomainValidationError


class TestTextField:

    @pytest.fixture
    def text_field(self) -> TextField:
        return TextField(
            make_test_metadata(),
            TEST_NAMES[0],
            TEST_CONTENTS[0]
        )
        
    def test_initialization(self, text_field: TextField):
        assert text_field.name == TEST_NAMES[0]
        assert text_field.content == TEST_CONTENTS[0]

    def test_update_content(self, text_field: TextField):
        text_field.update_content(TEST_CONTENTS[1])
        assert text_field.content == TEST_CONTENTS[1]

    def test_invalid_content_type_on_initialization(self):
        with pytest.raises(DomainValidationError):
            TextField(make_test_metadata(), TEST_NAMES[0], TEST_CONTENTS[5])

    def test_invalid_content_type_on_update(self):
        text_field = TextField(
            make_test_metadata(),
            TEST_NAMES[0],
            TEST_CONTENTS[0],
        )

        with pytest.raises(DomainValidationError):
            text_field.update_content(TEST_CONTENTS[5])
