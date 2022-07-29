from typing import Any, Dict, List

from app.models.user        import User
from app.dtos.address_dto   import AddressDTO
from app.dtos.role_dto      import RoleDTO


class UserDTO():
    def __init__(self) -> None:
        self.user_id     = None
        self.username    = None
        self.firstname   = None
        self.lastname    = None
        self.password    = None
        self.mail        = None
        self.description = None
        self.hours       = 0
        self.address: AddressDTO   = AddressDTO()
        self.roles: List[RoleDTO]  = []

    def getDTO(self):
        return self

    def getJSON(self):
        return self.__dict__

    @staticmethod
    def entity_to_dto(user: User):
        userdto = UserDTO()

        userdto.user_id     = user.user_id
        userdto.username    = user.username
        userdto.mail        = user.mail
        userdto.firstname   = user.first_name
        userdto.lastname    = user.last_name
        userdto.description = user.description
        userdto.hours       = user.hours
        userdto.address     = AddressDTO.entity_to_dto(user.address)
        userdto.roles       = [RoleDTO.entity_to_dto(role.rel_role) for role in user.roles]

        return userdto

    def dto_to_entity(self) -> User:
        user = User()

        user.user_id     = self.user_id
        user.username    = self.username
        user.password    = self.password
        user.first_name  = self.firstname
        user.last_name   = self.lastname
        user.mail        = self.mail
        user.hours       = self.hours
        user.description = self.description

        user.address     = self.address.dto_to_entity()
        user.roles       = [RoleDTO.dto_to_entity]

        # user.address.street  = self.address.street
        # user.address.number  = self.address.number
        # user.address.zip     = self.address.zip
        # user.address.country = self.address.country
        return user

    def get_attributes(self):
        return {
        "username":     self.username,
        "firstname":    self.firstname,
        "lastname":     self.lastname,
        "mail":         self.mail,
        "description":  self.description,
        "street":       self.address.street,
        "number":       self.address.number,
        "zip_code":     self.address.zip,
        "country":      self.address.country,
        }

    def load_from_attr_dict(self, dict: Dict[Any, Any]):
        self.username        = dict['username']
        self.firstname       = dict['firstname']
        self.lastname        = dict['lastname']
        self.mail            = dict['mail']
        self.description     = dict['description']
        self.address.street  = dict['street']
        self.address.number  = dict['number']
        self.address.zip     = dict['zip_code']
        self.address.country = dict['country']

        return self

    def get_roles(self):
        return [role.rolename for role in self.roles]