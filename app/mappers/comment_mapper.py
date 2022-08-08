from app.dtos.comment_dto import CommentDTO
from app.forms.comment.comment_add_form import CommentAddForm
from app.mappers.abstract_mapper import AbstractMapper
from app.models.comment import Comment


class CommentMapper(AbstractMapper):
    @staticmethod
    def entity_to_dto(comment: Comment):
        return CommentDTO.build_from_entity(comment)

    @staticmethod
    def form_to_entity(form, comment: Comment):
        if isinstance(form, CommentAddForm):
            comment.content = form.content.data

        return comment

    @staticmethod
    def content_data_to_entity(content, comment: Comment):
        comment.content = content

        return comment