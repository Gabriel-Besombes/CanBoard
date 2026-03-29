from app.domain.entities.card_elements.card_element import CardElement
from app.domain.values.metadata import MetaData
from app.domain.values.name import Name
from app.domain.errors import DomainValidationError

class TextField(CardElement):
    """Domain entity representing a text field card element."""
    
    def __init__(self, metadata: MetaData, name: Name, content: str):
        self._check_is_string(content)
        super().__init__(metadata, name, content)
    
    #region GETTERS
    @property
    def content(self) -> str:
        return self._content
    #endregion
    
    #region SETTERS
    def update_content(self, new_content: str):
        self._check_is_string(new_content)
        self._content = new_content
    #endregion
    
    @staticmethod
    def _check_is_string(content: str) -> bool:
        if not isinstance(content, str):
            raise DomainValidationError("Content for TextField must be a string.")
        return True