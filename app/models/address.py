from app import db
from app.models.base_entity import BaseEntity

class Address(db.Model, BaseEntity):
    __tablename__ = "address"
    address_id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(50))
    number = db.Column(db.Integer)
    zip = db.Column(db.Integer)
    country = db.Column(db.String(50))