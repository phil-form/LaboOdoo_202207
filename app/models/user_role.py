from app import db
from app.models.base_entity import BaseEntity

class UserRole(db.Model, BaseEntity):
    __tablename__ = "user_roles"
    user_role_id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.ForeignKey("roles.role_id"),nullable=False)
    user_id = db.Column(db.ForeignKey("users.user_id"),nullable=False)

    rel_role = db.relation('Role', back_populates='users')
    rel_user = db.relation('User', back_populates='roles')

    db.UniqueConstraint('user_id', 'service_id', name='uk_user_roles')
