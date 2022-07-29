from app                    import db
from app.models.base_entity import BaseEntity

class Delivery(db.Model, BaseEntity):
    __tablename__ = "deliveries"
    delivery_id        = db.Column(db.Integer, primary_key=True)
    client_id          = db.Column(db.ForeignKey('users.user_id'))
    user_service_id    = db.Column(db.ForeignKey('user_services.user_service_id'))
    start_date         = db.Column(db.DateTime(timezone=True))
    duration           = db.Column(db.Integer, nullable=False)
    duration_effective = db.Column(db.Integer)
    done               = db.Column(db.Boolean, nullable=False, default=False)
    rating             = db.Column(db.Integer)

    #client             = db.relationship("User"       , back_populates="deliveries")
    #user_serv          = db.relationship("UserService", back_populates="deliveries")
    client             = db.relationship("User")
    user_serv          = db.relationship("UserService")
