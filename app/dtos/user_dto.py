from app.dtos.address_dto import AddressDTO
from app.models.address import Address
from app.models.user import User

class UserDTO():
    def __init__(self) -> None:
        self.user_id = None
        self.username = None
        self.firstname = None
        self.lastname = None
        self.password = None
        self.mail = None
        self.description = None
        self.hours = 0
        self.address = AddressDTO()

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

    def dto_to_entity(self) -> User:
        user = User()

        user.user_id = self.user_id
        user.username = self.username
        user.first_name = self.firstname
        user.last_name = self.lastname
        user.mail = self.mail
        user.description = self.description
        user.hours = self.hours
        user.password = self.password

        user.address = Address()
        user.address.street = self.address.street
        user.address.number = self.address.number
        user.address.zip = self.address.zip
        user.address.country = self.address.country

        return user