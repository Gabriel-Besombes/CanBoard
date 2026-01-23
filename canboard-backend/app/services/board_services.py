from app.domain.board import Board

class BoardServices:
    
    def __init__(self, repo):
        self.repo = repo
        
    def create_board(self, name: str, description: str) -> Board:
        board = self.repo.create(name=name, description=description)
        return board