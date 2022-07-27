from app.models.address import Address

class AddressDTO():
    def __init__(self) -> None:
        self.address_id = None
        self.street = None
        self.number = None
        self.zip = None
        self.locality = None
        self.country = None

    def getDTO(self):
        return self

    def getJSON(self):
        return self.__dict__

    def getString(self):
        return f"{self.street} {self.number}\n{self.zip} {self.locality}\n{self.country}"

    @staticmethod
    def entity_to_dto(address: Address):
        addressdto = AddressDTO()

        addressdto.addressid = address.address_id
        addressdto.street = address.street 
        addressdto.number = address.number 
        addressdto.zip = address.zip
        addressdto.locality = address.locality 
        addressdto.country = address.country

        return addressdto