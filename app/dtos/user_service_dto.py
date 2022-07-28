from app.dtos.abstract_dto      import AbstractDTO
from app.models.user_service    import UserService

class UserServiceDTO(AbstractDTO):
    def __init__(self):
        self.user_service_id = None
        self.user_id         = None
        self.service_id      = None

    @staticmethod
    def build_from_entity(user_service: UserService):
        user_service_dto = UserServiceDTO()

        user_service_dto.user_service_id = user_service.user_service_id
        user_service_dto.user_id         = user_service.user_id
        user_service_dto.service_id      = user_service.service_id
        return user_service_dto

    def get_json_parsable(self):
        return self.__dict__

    def __str__(self):
        return f"{self.user_service_id} - {self.user_id} {self.service_id}"
