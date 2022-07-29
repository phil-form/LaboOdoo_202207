from app.models.address import Address

class AddressDTO():
    def __init__(self) -> None:
        self.address_id = None
        self.street     = None
        self.number     = None
        self.zip        = None
        self.locality   = None
        self.country    = None

    def getDTO(self):
        return self

    def getJSON(self):
        return self.__dict__

    def getString(self):
        return f"{self.street} {self.number}\n{self.zip} {self.locality}\n{self.country}"

    @staticmethod
    def entity_to_dto(address: Address):
        dto = AddressDTO()

        dto.address_id = address.address_id
        dto.street     = address.street 
        dto.number     = address.number 
        dto.zip        = address.zip
        dto.locality   = address.locality 
        dto.country    = address.country

        return dto

    def dto_to_entity(self):
        entity = Address()

        entity.address_id = self.address_id
        entity.street     = self.street
        entity.number     = self.number
        entity.zip        = self.zip
        entity.locality   = self.locality
        entity.country    = self.country

        return entity
