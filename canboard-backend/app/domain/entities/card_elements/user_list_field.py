from app.domain.entities.card_elements.card_element import CardElement
from app.domain.collections.user_collection import UserCollection
from app.domain.values import MetaData, Name
from app.domain.errors import DomainValidationError


class UserListField(CardElement):
    """Domain entity representing a user list card element."""
    
    def __init__(self, metadata: MetaData, name: Name, content: UserCollection):
        self._check_is_user_collection(content)
        super().__init__(metadata, name, content)
    
    #region GETTERS
    @property
    def content(self) -> UserCollection:
        return self._content
    #endregion
    
    #region SETTERS
    def update_content(self, new_content: UserCollection):
        self._check_is_user_collection(new_content)
        self._content = new_content
    #endregion
    
    @staticmethod
    def _check_is_user_collection(content: UserCollection) -> bool:
        if not isinstance(content, UserCollection):
            raise DomainValidationError("Content for UserListField must be a UserCollection.")
        return True