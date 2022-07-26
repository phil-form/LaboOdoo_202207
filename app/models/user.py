from app import db
from app.models.base_entity import BaseEntity

class User(db.Model, BaseEntity):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False, index=True)