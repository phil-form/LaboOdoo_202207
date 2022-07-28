from app.mappers.abstract_mapper    import AbstractMapper

from app.dtos.delivery_dto          import DeliveryDTO
#from app.forms
from app.models.delivery            import Delivery

class DeliveryMapper(AbstractMapper):
    @staticmethod
    def entity_to_dto(entity: Delivery):
        return DeliveryDTO.build_from_entity(entity)

    @staticmethod
    def form_to_entity(form, delivery: Delivery):
        delivery.client_id          = int                    (form.clientname.data)
        delivery.start_date         =                         form.startdate.data
        delivery.duration           = DeliveryMapper.conv_dur(form.duration.data)
        delivery.duration_effective = DeliveryMapper.conv_dur(form.durationeff.data)
        delivery.done               =                         form.done.data

    @staticmethod
    def conv_dur(dur_str: str) -> int:
        if dur_str == None:
            return None

        hm = dur_str.split(":")
        h  = int(hm[0])
        m  = int(hm[1])

        return (60 * h) + m
