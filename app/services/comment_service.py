from app import db
from app.dtos.comment_dto import CommentDTO
from app.mappers.comment_mapper import CommentMapper
from app.models.comment import Comment
from app.services.base_service import BaseService


class CommentService(BaseService):
    def find_all(self):
        return [CommentDTO.build_from_entity(comment) for comment in Comment.query.all()]

    def find_one(self, entity_id: int):
        return CommentDTO.build_from_entity(Comment.query.filter_by(comment_id=entity_id).one())

    def find_all_by(self, **kwargs):
        return [CommentDTO.build_from_entity(comment) for comment in Comment.query.filter_by(**kwargs)]

    def find_one_by(self, **kwargs):
        return CommentDTO.build_from_entity(Comment.query.filter_by(**kwargs).one())

    def insert(self, data):
        comment = Comment()
        CommentMapper.form_to_entity(data, comment)
        comment.author_id = 1
        comment.service_id = 1

        try:
            db.session.add(comment)
            db.session.commit()
        except Exception as e:
            print(e)
            raise e
            db.session.rollback()

        return self.find_one(comment.comment_id)

    def update(self, entity_id: int, content):
        comment = Comment.query.filter_by(comment_id=entity_id).one()

        if comment is None:
            return None

        CommentMapper.content_data_to_entity(content, comment)

        try:           
            db.session.commit()
        except Exception as e:
            print(e)
            raise e
            db.session.rollback()

        return self.find_one(entity_id)

    def delete(self, entity_id: int):
        comment = Comment.query.filter_by(comment_id=entity_id).one()

        if comment is None:
            return None

        try:
            db.session.delete(comment)
            db.session.commit()
        except Exception as e:
            print(e)
            raise e
            db.session.rollback()

        return comment.comment_id