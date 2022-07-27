from app.services.base_service import BaseService
from app.models.user import User
from app.dtos.user_dto import UserDTO
from app import db
from bcrypt import gensalt, hashpw


class UserService(BaseService):
    def find_one(self, entity_id: int):
        return UserDTO.entity_to_dto(User.query.filter_by(user_id= entity_id).one())

    def find_all(self):
        pass

    def find_one_by(self, **kwargs):
        pass

    def insert(self, data: UserDTO):
        print(data.password)
        user = data.dto_to_entity()
        encrypted_pass = hashpw(user.password.encode('utf-8'), gensalt()).decode('utf-8')
        user.password = encrypted_pass
        print(user.password)

    def update(self, entity_id: int, data):
        pass

    def delete(self, entity_id: int):
        pass