from app.dtos.abstract_dto      import AbstractDTO
from app.dtos.user_dto          import UserDTO
from app.dtos.service_dto       import ServiceDTO
from app.dtos.user_service_dto  import UserServiceDTO
from app.models.delivery        import Delivery

class DeliveryDTO(AbstractDTO):
    def __init__(self):
        self.delivery_id        = None
        self.client_id          = None
        self.user_service_id    = None
        self.start_date         = None
        self.duration           = None
        self.duration_effective = None
        self.done               = None
        self.rating             = None

        self.client             = UserDTO()
        self.user_serv          = UserServiceDTO()
        #self.user               = UserDTO()
        #self.service            = ServiceDTO()
    
    @staticmethod
    def build_from_entity(entity):
        delivery_dto = DeliveryDTO()

        if isinstance(entity, Delivery):
            delivery_dto.delivery_id        = entity.delivery_id
            delivery_dto.client_id          = entity.client_id
            delivery_dto.user_service_id    = entity.user_service_id
            delivery_dto.start_date         = entity.start_date
            delivery_dto.duration           = entity.duration
            delivery_dto.duration_effective = entity.duration_effective
            delivery_dto.done               = entity.done
            delivery_dto.rating             = entity.rating

            delivery_dto.client             = UserDTO.entity_to_dto           (entity.client)
            delivery_dto.user_serv          = UserServiceDTO.build_from_entity(entity.user_serv)

        return delivery_dto

    def get_json_parsable(self):
        return self.__dict__
