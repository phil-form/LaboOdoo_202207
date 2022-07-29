from app import db
from app.models.base_entity import BaseEntity


class Message(db.Model, BaseEntity):
    __tablename__ = "messages"
    message_id = db.Column(db.Integer, primary_key=True)
    from_user_id = db.Column(db.ForeignKey('users.user_id'), nullable=False)
    to_user_id = db.Column(db.ForeignKey('users.user_id'), nullable=False)
    content = db.Column(db.Text, nullable=False)

    from_user = db.relationship('User', foreign_keys=[from_user_id])
    to_user = db.relationship('User', foreign_keys=[to_user_id])

    def __str__(self):
        return f'[Message] from {self.from_user.username} to {self.to_user.username} : \"{self.content}\"'
