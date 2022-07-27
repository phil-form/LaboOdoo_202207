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
        delivery.client_id          = int     (form.client_str.data)
        delivery.start_date         =          form.start_date.data
        delivery.duration           = conv_dur(form.dur_str.data)
        delivery.duration_effective = conv_dur(form.dur_eff_str.data)
        delivery.done               =          form.done.data
        # if isinstance(form, BasketAddItemForm):
        #

    def conv_dur(DurStr: str) -> int:
        hm = DurStr.split(":")
        h  = int(hm[0])
        m  = int(hm[1])

        return (60 * h) + m
