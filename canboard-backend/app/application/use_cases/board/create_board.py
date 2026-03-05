from app.domain.board import Board
from app.domain.repositories.board_repository import BoardRepository
from app.domain.values.name import Name
from app.domain.values.description import Description
from app.application.commands.create_board_command import CreateBoardCommand
from app.application.dtos.board_dto import BoardDTO

class CreateBoardUseCase:
    """Use case for creating a new board."""
    
    def __init__(self, board_repository: BoardRepository):
        self.board_repository = board_repository
    
    async def execute(self, command: CreateBoardCommand) -> BoardDTO:
        """
        Execute the create board use case.
        
        Args: 
            command: CreateBoardCommand containing name and description
            
        Returns:
            CreateBoardOutput with the created board's details
            
        Raises:
            ValueError: If name or description are invalid
        """
        # Create domain value objects (validates input)
        name = Name(command.name)
        description = Description(command.description)
        
        # Create domain entity
        board = Board(name=name, description=description)
        
        # Persist through repository
        await self.board_repository.save(board)
        
        # Return output DTO
        return BoardDTO(
            board_id=str(board.id.value),
            name=board.name.value,
            description=board.description.value
        )