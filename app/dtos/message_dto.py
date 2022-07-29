from app.dtos.abstract_dto import AbstractDTO
from app.dtos.user_dto import UserDTO
from app.models.message import Message


class MessageDTO(AbstractDTO):

    def __init__(self):
        self.message_id = None
        self.content = None
        self.from_user = None
        self.to_user = None

    @staticmethod
    def build_from_entity(message: Message):
        message_dto = MessageDTO()
        message_dto.message_id = message.message_id
        message_dto.content = message.content
        message_dto.from_user = UserDTO.entity_to_dto(message.from_user)
        message_dto.to_user = UserDTO.entity_to_dto(message.to_user)
        return message_dto

    @staticmethod
    def get_json_parsable(self):
        pass
