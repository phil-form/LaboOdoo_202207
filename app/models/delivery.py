from app                    import db
from app.models.base_entity import BaseEntity

class Delivery(db.Model, BaseEntity):
    __tablename__ = "deliveries"
    delivery_id        = db.Column(db.Integer, primary_key=True)
    client_id          = db.Column(db.ForeignKey('users.user_id'))
    user_service_id    = db.Column(db.ForeignKey('user_services.user_service_id'))
    done               = db.Column(db.Boolean, nullable=False, default=False)
    duration           = db.Column(db.Integer, nullable=False)
    duration_effective = db.Column(db.Integer)
    rating             = db.Column(db.Integer)
