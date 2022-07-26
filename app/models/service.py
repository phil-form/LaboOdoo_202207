from app import db
from app.models.base_entity import BaseEntity


class Service(BaseEntity, db.Models):
    __tablename__ = "services"
    service_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False, index=True)
    service_type = db.Column(db.ForeignKey('service_types.service_type_id'), nullable=False)
    request = db.Column(db.Boolean, nullable=False, default=False)
    description = db.Column(db.Text)
