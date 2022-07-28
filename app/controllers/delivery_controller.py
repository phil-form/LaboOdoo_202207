from flask                              import render_template, redirect, request
from flask_wtf                          import FlaskForm

from app                                import app
from app.framework.decorators.inject    import inject
from app.models.delivery                import Delivery
from app.services.delivery_service      import DeliveryService
from app.forms.delivery_add_update      import DeliveryAddUpdateForm
from app.services.user_service          import UserService
from app.services.service_service       import ServiceService
from app.services.service_type_service  import ServiceTypeService

@app.route('/delivery/add/<int:user_service_id>', methods=['GET', 'POST'])
@inject
def delivery_add(user_service_id, delivery_serv: DeliveryService):
    frm = DeliveryAddUpdateForm(request.form)
    if request.method == 'POST':
        if frm.validate():
            delivery = delivery_serv.insert(frm)
            return redirect(url_for('#', delivery_id=delivery.delivery_id))

    return delivery_add_update(frm, user_service_id, -1)

@app.route('/delivery/update/<int:delivery_id>', methods=['GET', 'POST'])
@inject
def delivery_update(delivery_id, delivery_serv: DeliveryService):
    frm = DeliveryAddUpdateForm(request.form)
    if request.method == 'POST':
        if frm.validate():
            delivery = delivery_serv.update(delivery.delivery_id, frm)
            return redirect(url_for('#', delivery_id=delivery.delivery_id))

    return delivery_add_update(frm, -1, delivery_id)

@inject
def delivery_add_update(frm, user_service_id, delivery_id, 
                        dlv_srv: DeliveryService, 
                        usr_srv: UserService, 
                        svc_svc: ServiceService, 
                        svc_typ: ServiceTypeService):
    if delivery_id == -1:
        # add
        delivery = Delivery()
        delivery.user_service_id = user_service_id
        cl_id = -1
    else:
        # update
        delivery = dlv_srv.find_one(delivery_id)
        cl_id = delivery.client_id

    usr_srv = svc_svc.find_one_user_service(delivery.user_service_id)
    user    = usr_srv.find_one(usr_srv.rel_user)
    service = svc_svc.find_one(usr_srv.rel_service)
    srv_typ = svc_typ.find_one(service.service_type)

    usr_lst = usr_srv.find_all()

    return render_template('delivery/add_update.html',  form=frm,
                                                        clid=cl_id,
                                                        user=user,
                                                        service=service,
                                                        srvtype=srv_typ.name,
                                                        delivery=delivery,
                                                        usr_lst=usr_lst)
