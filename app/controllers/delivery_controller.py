from flask                              import render_template, redirect, request
from flask_wtf                          import FlaskForm

from app                                import app
from app.framework.decorators.inject    import inject
from app.models.delivery                import Delivery
from app.services.delivery_service      import DeliveryService
from app.forms.delivery_add_update      import DeliveryAddUpdateForm
from app.services.user_service          import UserService
# ces services n'existent pas encore
#from app.services.service_service       import ServiceService
#from app.services.service_type_service  import ServiceTypeService
#from app.services.user_service_service  import UserServiceService

# ne sera (probablement ?) plus utile lorsque les sercices ci-dessus existeront
from app.models.user                    import User
from app.models.service                 import Service
from app.models.service_type            import ServiceType

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
def delivery_add_update(frm, user_service_id, delivery_id, delivery_serv: DeliveryService, usr_srv: UserService):
    if delivery_id == -1:
        # add
        delivery = Delivery()
        delivery.user_service_id = user_service_id
        cl_id = -1
    else:
        # update
        #delivery = delivery_serv.find_one(delivery_id)
        delivery = Delivery()               # temporaire
        delivery.delivery_id = 1            # temporaire
        delivery.user_service_id = 1        # temporaire
        delivery.client_id = 3              # temporaire
        delivery.start_date = "2023-01-01"  # temporaire
        delivery.duration = 4               # temporaire
        cl_id = delivery.client_id

    # il n'y a pas encore de user_service_service ...
    # usr_srv      = user_service_service.find_one(delivery.user_service_id)
    usr_srv      = UserService() # temporaire
    usr_srv.rel_user = 1         # temporaire
    usr_srv.rel_service = 1      # temporaire

    # user        = UserService.find_one(usr_srv.rel_user)
    user = User()               # temporaire
    user.user_id = 1            # temporaire
    user.first_name = "Etienne" # temporaire
    user.last_name = "André"    # temporaire

    # il n'y a pas encore de service_service ...
    # service     = service_service.find_one(usr_srv.rel_service)
    service     = Service()             # temporaire
    service.service_id = 1              # temporaire
    service.name = "Tondre la pelouse"  # temporaire
    # serviceType = ServiceTypeService.find_one(service.service_type)
    serviceType = ServiceType()         # temporaire
    serviceType.name = "Jardinage"      # temporaire

    #usr_lst = usr_srv.find_all()
    usr_lst = []                    # temporaire
    usr = User()                    # temporaire
    usr.user_id = -1                # temporaire
    usr.first_name = "Choisissez"   # temporaire
    usr.last_name = ""              # temporaire
    usr_lst.append(usr)             # temporaire
    usr = User()                    # temporaire
    usr.user_id = 2                 # temporaire
    usr.first_name = "Alfred"       # temporaire
    usr.last_name = "Dupont"        # temporaire
    usr_lst.append(usr)             # temporaire
    usr = User()                    # temporaire
    usr.user_id = 3                 # temporaire
    usr.first_name = "Barnabé"      # temporaire
    usr.last_name = "Martin"        # temporaire
    usr_lst.append(usr)             # temporaire
    usr = User()                    # temporaire
    usr.user_id = 4                 # temporaire
    usr.first_name = "Casimir"      # temporaire
    usr.last_name = "Durand"        # temporaire
    usr_lst.append(usr)             # temporaire

    return render_template('delivery/add_update.html',  form=frm,
                                                        clid=cl_id,
                                                        user=user,
                                                        service=service,
                                                        srvtype=serviceType.name,
                                                        delivery=delivery,
                                                        usr_lst=usr_lst)
