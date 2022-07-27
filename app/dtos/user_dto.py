from app.dtos.address_dto import AddressDTO
from app.models.user import User

class UserDTO():
    def __init__(self) -> None:
        self.user_id = None
        self.username = None
        self.firstname = None
        self.lastname = None
        self.mail = None
        self.description = None
        self.hours = None
        self.address: AddressDTO = None

    def getDTO(self):
        return self

    def getJSON(self):
        return self.__dict__

    @staticmethod
    def entity_to_dto(user: User):
        userdto = UserDTO()

        userdto.user_id = user.user_id
        userdto.username = user.username
        userdto.firstname = user.first_name
        userdto.lastname = user.last_name
        userdto.mail = user.mail
        userdto.description = user.description
        userdto.hours = user.hours
        userdto.address = AddressDTO.entity_to_dto(user.address)

        return userdto

