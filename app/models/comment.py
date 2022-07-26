from app import db
from app.models.base_entity import BaseEntity

class Comment(db.Model, BaseEntity):
    __tablename__ = "comments"
    comment_id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.ForeignKey('users.user_id'))
    user_service_id = db.Column(db.ForeignKey('users_services.user_service_id'))
    service_id = db.Column(db.ForeignKey('services.service_id'))
    content = db.Column(db.String(500), nullable=False)