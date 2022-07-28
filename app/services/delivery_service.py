from flask                          import session

from app                            import db
from app.services.base_service      import BaseService

from app.models.delivery            import Delivery
from app.mappers.delivery_mapper    import DeliveryMapper
from app.dtos.delivery_dto          import DeliveryDTO

class DeliveryService(BaseService):
    def find_all(self):
        return [DeliveryDTO.build_from_entity(delivery) for delivery in Delivery.query.all()]

    def find_one(self, entity_id: int):
        return DeliveryDTO.build_from_entity(Delivery.query.filter_by(delivery_id=entity_id).one())

    def find_one_by(self, **kwargs):
        return DeliveryDTO.build_from_entity(Delivery.query.filter_by(**kwargs).one())

    def insert(self, data):
        delivery = Delivery()
        DeliveryMapper.form_to_entity(data, delivery)
        print(delivery)
        try:
            db.session.add(delivery)
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()

        return self.find_one(delivery.delivery_id)

    def update(self, entity_id: int, data):
        delivery = Delivery.query.filter_by(delivery_id=entity_id).one()
        if delivery is None:
            return None

        DeliveryMapper.form_to_entity(data, delivery)
        try:
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
        
        return self.find_one(entity_id)

    def delete(self, entity_id: int):
        delivery = Delivery.query.filter_by(delivery_id=entity_id).one()
        if delivery is None:
            return None

        try:
            db.session.delete(delivery)
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()

        return delivery.delivery_id
