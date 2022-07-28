from app.services.base_service import BaseService
from app.models.user import User
from app.dtos.user_dto import UserDTO
from app import db
from bcrypt import gensalt, hashpw, checkpw
from app.forms.user_login_form import UserLoginform


class UserService(BaseService):
    def find_one(self, entity_id: int):
        return UserDTO.entity_to_dto(User.query.filter_by(user_id= entity_id).one())

    def find_all(self):
        pass

    def find_one_by(self, **kwargs):
        pass

    def insert(self, data: UserDTO):
        user = data.dto_to_entity()
        encrypted_pass = hashpw(user.password.encode('utf-8'), gensalt()).decode('utf-8')
        user.password = encrypted_pass

        try:
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()

    def login(self, data: UserLoginform):
        user = User.query.filter_by(username=data.login.data).first()
        if not user:
            user = User.query.filter_by(mail=data.login.data).first()
        if not user:
            return {"errors": f"username '{data.login.data}' does not exist"}
        
        if checkpw(data.password.data.encode('utf-8'), user.password.encode('utf-8')):
            return UserDTO.entity_to_dto(user)
        return {"errors" : "wrong password"}

    def update(self, entity_id: int, data):
        pass

    def delete(self, entity_id: int):
        pass