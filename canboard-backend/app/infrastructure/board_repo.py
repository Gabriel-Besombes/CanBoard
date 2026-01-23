from app.domain.board import Board

class InMemoryBoardRepo:
    def __init__(self):
        self.boards: dict[int, Board] = {}
        self.next_id = 1

    def create(self, name: str, description: str) -> Board:
        board = Board(id=self.next_id, name=name, description=description)
        self.boards[self.next_id] = board
        self.next_id += 1
        return board

    def get(self, board_id: int) -> Board | None:
        return self.boards.get(board_id)

    def update(self, board_id: int, name: str = None, description: str = None) -> Board | None:
        board = self.boards.get(board_id)
        if not board:
            return None
        if name:
            board.name = name
        if description:
            board.description = description
        return board

    def delete(self, board_id: int) -> Board | None:
        return self.boards.pop(board_id, None)