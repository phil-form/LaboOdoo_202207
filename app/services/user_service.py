from app.services.base_service import BaseService
from app.models.user import User
from app.dtos.user_dto import UserDTO


class UserService(BaseService):
    def find_one(self, entity_id: int):
        return UserDTO.entity_to_dto(User.query.filter_by(user_id= entity_id).one())

    def find_all(self):
        pass

    def find_one_by(self, **kwargs):
        pass

    def insert(self, data):
        pass

    def update(self, entity_id: int, data):
        pass

    def delete(self, entity_id: int):
        pass