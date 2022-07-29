from app import db
from app.models.base_entity import BaseEntity

class Role(db.Model, BaseEntity):
    __tablename__ = "roles"
    role_id  = db.Column(db.Integer, primary_key=True)
    rolename = db.Column(db.String(50))

    users = db.relationship('UserRole', cascade='all')

    def add_role(rolename: str):
        role = Role()
        role.rolename = rolename

        try:
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
