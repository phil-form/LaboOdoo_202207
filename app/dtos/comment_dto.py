from app.dtos.abstract_dto import AbstractDTO
from app.models.comment import Comment


class CommentDTO(AbstractDTO):
    def __init__(self):
        self.comment_id = None
        self.author_id = None
        self.user_services_id = None
        self.service_id = None
        self.content = None

    @staticmethod
    def build_from_entity(entity):
        comment_dto = CommentDTO()

        if isinstance(entity, Comment):
            comment_dto.comment_id = entity.comment_id
            comment_dto.author_id = entity.rel_author.user_id
            comment_dto.author_name = entity.rel_author.username
            comment_dto.user_services_id = entity.user_service_id
            comment_dto.service_id = entity.service_id
            comment_dto.content = entity.content
            comment_dto.create_date = entity.createdate

        return comment_dto


    def get_json_parsable(self):
        return self.__dict__