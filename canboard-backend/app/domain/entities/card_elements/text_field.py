from app.domain.entities.card_elements.card_element import CardElement

class TextField(CardElement):
    """Domain entity representing a text field card element."""
    
    content: str