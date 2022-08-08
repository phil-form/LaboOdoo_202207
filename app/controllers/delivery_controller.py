from flask                              import render_template, redirect, request, url_for
from flask_wtf                          import FlaskForm

from app                                import app
from app.framework.decorators.inject    import inject
from app.forms.delivery_add_update      import DeliveryAddUpdateForm
from app.models.delivery                import Delivery
from app.services.delivery_service      import DeliveryService
from app.services.user_service          import UserService
from app.services.service_service       import ServiceService

@app.route('/delivery/list', methods=['GET', 'POST'])
@inject
def delivery_list(delivery_serv: DeliveryService):
    return render_template('delivery/list.html', delivers=delivery_serv.find_all())

@app.route('/delivery/add/<int:user_service_id>', methods=['GET', 'POST'])
@inject
def delivery_add(user_service_id, delivery_serv: DeliveryService):
    frm = DeliveryAddUpdateForm(request.form)
    if request.method == 'POST':
        if frm.validate():
            delivery = delivery_serv.insert(frm)
            return redirect(url_for('delivery_list'))

    return delivery_add_update(frm, user_service_id, -1)

@app.route('/delivery/update/<int:delivery_id>', methods=['GET', 'POST'])
@inject
def delivery_update(delivery_id, delivery_serv: DeliveryService):
    frm = DeliveryAddUpdateForm(request.form)
    if request.method == 'POST':
        if frm.validate():
            delivery = delivery_serv.update(delivery.delivery_id, frm)
            return redirect(url_for('delivery_list'))

    return delivery_add_update(frm, -1, delivery_id)

@inject
def delivery_add_update(frm, user_service_id, delivery_id, 
                        dlv_srv: DeliveryService, 
                        usr_svc: UserService, 
                        svc_svc: ServiceService):
    if delivery_id == -1:
        # add
        cl_id    = -1
        delivery = Delivery()
        delivery.user_service_id = user_service_id
    else:
        # update
        delivery = dlv_srv.find_one(delivery_id)
        cl_id    = delivery.client_id

    usr_srv = svc_svc.find_one_user_service(delivery.user_service_id)
    user    = usr_svc.find_one(usr_srv.rel_user)
    service = svc_svc.find_one(usr_srv.rel_service)

    dur_str = dur_to_str(delivery.duration)
    eff_str = dur_to_str(delivery.duration_effective)

    usr_lst = usr_svc.find_all()

    return render_template('delivery/add_update.html',  form=frm,
                                                        clid=cl_id,
                                                        user=user,
                                                        service=service,
                                                        delivery=delivery,
                                                        dur_str=dur_str,
                                                        eff_str=eff_str,
                                                        usr_lst=usr_lst)

def dur_to_str(dur: int) -> str:
    if dur == None:
        return ""
    if dur == 0:
        return ""

    mn = str(dur % 60)
    if int(mn) < 10:
        mn = "0" + mn
    return str(dur // 60) + ":" + mn
