from typing import Any, Dict
from app import db
from app.models.base_entity import BaseEntity
from app.models.user_role import UserRole
from app.models.role import Role

class User(db.Model, BaseEntity):
    __tablename__ = "users"

    user_id     = db.Column(db.Integer,     primary_key=True)
    username    = db.Column(db.String(50),  unique=True, nullable=False, index=True)
    password    = db.Column(db.String(256), nullable=False)
    first_name  = db.Column(db.String(50),  nullable=False)
    last_name   = db.Column(db.String(50),  nullable=False)
    mail        = db.Column(db.String(100))
    description = db.Column(db.Text)
    hours       = db.Column(db.Integer)

    address_id = db.Column(db.ForeignKey("address.address_id"))
    address    = db.relationship("Address", back_populates="users")

    services   = db.relationship('UserService', cascade='all')
    roles      = db.relationship('UserRole'   , cascade='all')

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
        self.username        = dict['username']
        self.first_name      = dict['firstname']
        self.last_name       = dict['lastname']
        self.mail            = dict['mail']
        self.description     = dict['description']
        self.address.street  = dict['street']
        self.address.number  = dict['number']
        self.address.zip     = dict['zip_code']
        self.address.country = dict['country']

        return self

    def add_role(self, role: Role):
        if role in self.roles:
            return

        userrole = UserRole()
        userrole.rel_role = role
        userrole.rel_user = self
        self.roles.append(userrole)

    def get_roles(self):
        return [role.rel_role.rolename for role in self.roles]