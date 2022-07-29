from app.mappers.abstract_mapper    import AbstractMapper
from app.dtos.delivery_dto          import DeliveryDTO
from app.models.delivery            import Delivery

class DeliveryMapper(AbstractMapper):
    @staticmethod
    def entity_to_dto(entity: Delivery):
        return DeliveryDTO.build_from_entity(entity)

    @staticmethod
    def form_to_entity(form, delivery: Delivery):
        delivery.user_service_id    = int                      (form.usrsrv.data)
        delivery.client_id          = int                      (form.clientname.data)
        delivery.start_date         =                           form.startdate.data
        delivery.duration           = DeliveryMapper.dur_to_int(form.duration.data)
        delivery.duration_effective = DeliveryMapper.dur_to_int(form.durationeff.data)
        delivery.done               =                           form.done.data

    @staticmethod
    def dur_to_int(dur_str: str) -> int:
        if dur_str == None:
            return None

        hm = dur_str.split(":")
        h  = int(hm[0])
        m  = int(hm[1])

        return (60 * h) + m

    def xyz():
        x = DeliveryDTO()
        x.client.firstname
        x.user_serv.rel_service.type
        x.user_serv.user.firstname
        x.user_serv.service.type
