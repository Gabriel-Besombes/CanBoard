from app.domain.card_elements.card_element import CardElement

class TextField(CardElement):
    """Domain entity representing a text field card element."""
    
    def __init__(self, id: int, name: str, content: str):
        """
        Initialize a TextField.
        
        Args:
            id: The unique identifier for the card element.
            name: The name of the card element.
            content: The text content of the text field.
        """
        super().__init__(id, name, content)

    @property
    def content(self) -> str:
        return self._content