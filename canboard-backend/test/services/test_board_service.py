from app.services.board_services import BoardServices

"""
Tests for the BoardServices.

Tested classes:
- app.services.board_services.BoardServices
"""

import pytest
from app.infrastructure.board_repo import InMemoryBoardRepo

TEST_BOARD_NAME = "Test Board"
TEST_BOARD_DESCRIPTION = "This is a test board."

@pytest.mark.tested_classes("BoardServices")
class TestBoardService:
    
    @pytest.fixture(autouse=True)
    def setup(self):
        repo = InMemoryBoardRepo()
        service = BoardServices(repo=repo)
        self.board = service.create_board(name=TEST_BOARD_NAME, description=TEST_BOARD_DESCRIPTION)

    def test_create_board(self):

        assert self.board.id == 1
        assert self.board.name == TEST_BOARD_NAME
        assert self.board.description == TEST_BOARD_DESCRIPTION