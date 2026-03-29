from app.domain.entities.base_entity import BaseEntity
from app.domain.values.metadata import MetaData
from app.domain.values.name import Name
from app.domain.values.email import Email
from app.domain.values.user_name import UserName
from app.domain.values.password_hash import PasswordHash



class User(BaseEntity):
    """User domain entity."""
    
    __slots__ = ("_name", "_email", "_user_name", "_password_hash",)

    def __init__(self, metadata: MetaData, name: Name, email: Email, user_name: UserName, password_hash: PasswordHash):
        super().__init__(metadata)
        self._name = name
        self._email = email
        self._user_name = user_name
        self._password_hash = password_hash

    @property
    def name(self) -> Name:
        return self._name

    @property
    def email(self) -> Email:
        return self._email

    @property
    def user_name(self) -> UserName:
        return self._user_name

    @property
    def password_hash(self) -> PasswordHash:
        return self._password_hash

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.id}, name={self._name}, email={self._email}, user_name={self._user_name}, password_hash={self._password_hash})"