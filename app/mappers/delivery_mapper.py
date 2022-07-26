from app.mappers.abstract_mapper    import AbstractMapper

from app.dtos.delivery_dto          import DeliveryDTO
#from app.forms
from app.models.delivery            import Delivery

class DeliveryMapper(AbstractMapper):
    @staticmethod
    def entity_to_dto(entity: Delivery()):
        return DeliveryDTO.build_from_entity(entity)

    @staticmethod
    def form_to_entity(form, delivery: Delivery):
        pass
        # if isinstance(form, BasketAddItemForm):
        #
