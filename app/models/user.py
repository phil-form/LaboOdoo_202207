from app import db
from app.models.base_entity import BaseEntity

class User(db.Model, BaseEntity):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False, index=True)
    password = db.Column(db.String(256), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    mail = db.Column(db.String(100))
    description = db.Column(db.Text)
    hours = db.Column(db.Integer)
    address = db.Column(db.ForeignKey("address.address_id"))