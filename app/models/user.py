from typing import Any, Dict
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

    address_id = db.Column(db.ForeignKey("address.address_id"))
    address = db.relationship("Address", back_populates="users")

    services = db.relationship('UserService', cascade='all')

    def get_attributes(self):
        return {
        "username":     self.username,
        "firstname":    self.first_name,
        "lastname":     self.last_name,
        "mail":         self.mail,
        "description":  self.description,
        "street":       self.address.street,
        "number":       self.address.number,
        "zip_code":     self.address.zip,
        "country":      self.address.country,
        }

    def load_from_attr_dict(self, dict: Dict[Any, Any]):
        self.username       = dict['username']
        self.first_name       = dict['firstname']
        self.last_name        = dict['lastname']
        self.mail            = dict['mail']
        self.description     = dict['description']
        self.address.street  = dict['street']
        self.address.number  = dict['number']
        self.address.zip     = dict['zip_code']
        self.address.country = dict['country']

        return self