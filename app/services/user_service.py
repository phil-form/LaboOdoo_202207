from app.services.base_service import BaseService
from app.models.user import User
from app.dtos.user_dto import UserDTO


class UserService(BaseService):
    def find_one(self, entity_id: int):
        return UserDTO.entity_to_dto(User.query.filter_by(user_id= entity_id).one())