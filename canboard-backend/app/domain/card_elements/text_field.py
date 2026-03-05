from app.domain.card_elements.card_element import CardElement
from app.domain.values.name import Name
from app.domain.values.entity_id import EntityId

class TextField(CardElement):
    """Domain entity representing a text field card element."""
    
    def __init__(self, name: Name, content: str, id: EntityId | None = None):
        """
        Initialize a TextField.
        
        Args:
            id: The unique identifier for the card element.
            name: The name of the card element.
            content: The text content of the text field.
        """
        super().__init__(id=id, name=name, content=content)

    @property
    def content(self) -> str:
        return self._content