from app.domain.collections.base_entity_collection import BaseEntityCollection
from app.domain.entities.user import User

class UserCollection(BaseEntityCollection[User]):
    """Collection of users."""
    _entity_type = User