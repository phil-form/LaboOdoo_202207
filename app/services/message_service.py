from flask import session
from sqlalchemy import or_

from app import db
from app.dtos.message_dto import MessageDTO
from app.forms.message_form import MessageForm
from app.models.message import Message
from app.models.user import User
from app.services.base_service import BaseService


class MessageService(BaseService):
    def find_all(self):
        return [MessageDTO.build_from_entity(message) for message in Message.query.all()]

    def find_all_between(self, user1_id, user2_id):
        messages = Message.query.filter(or_(
            Message.from_user_id == user1_id,
            Message.from_user_id == user2_id
        ), or_(
            Message.to_user_id == user1_id,
            Message.to_user_id == user2_id
        )).order_by(Message.createdate.desc())

        return [MessageDTO.build_from_entity(message) for message in messages]

    def find_one(self, message_id: int):
        return MessageDTO.build_from_entity(Message.query.filter_by(message_id=message_id).one())

    def find_one_by(self, **kwargs):
        return MessageDTO.build_from_entity(Message.query.filter_by(**kwargs).one())

    def insert(self, form):
        message = Message()
        if isinstance(form, MessageForm):
            message.content = form.content.data
        message.from_user = User.query.filter_by(user_id=session.get('userid'))
        message.to_user = User.query.filter_by(user_id=form.to_user_id.data)
        try:
            db.session.add(message)
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
        return self.find_one(message.message_id)

    def update(self, message_id: int, form):
        message = Message.query.filter_by(message_id=message_id).one()
        if message is None:
            return None

        if isinstance(form, MessageForm):
            message.content = form.content.data
        try:
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()

        return self.find_one(message_id)

    def delete(self, message_id: int):
        message = Message.query.filter_by(message_id=message_id).one()
        if message is None:
            return None
        try:
            db.session.delete(message)
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()

        return message.message_id