from flask                              import render_template, redirect
from flask_wtf                          import FlaskForm

from app                                import app
from app.models.delivery                import Delivery
from app.services.delivery_service      import DeliveryService
from app.forms.delivery_add_update      import DeliveryAddUpdateForm
# ces services n'existent pas encore
#from app.services.user_service          import UserService
#from app.services.service_service       import ServiceService
#from app.services.user_service_service  import UserServiceService

# ne sera plus utile lorsque les sercices ci-dessus existeront
from app.models.user_service import UserService
from app.models.user import User
from app.models.service import Service

@app.route('/delivery/add', methods=['GET', 'POST'])
def deliveryAdd(user_service_id):
    return deliveryAddUpdate(user_service_id, -1)

@app.route('/delivery/update', methods=['GET', 'POST'])
def deliveryUpdate(delivery_id):
    return deliveryAddUpdate(-1, delivery_id)

def deliveryAddUpdate(user_service_id, delivery_id):
    if delivery_id == -1:
        # add
        delivery = Delivery()
        delivery.user_service_id = user_service_id
    else:
        # update
        delivery = DeliveryService.find_one(delivery_id)

    frm         = DeliveryService(FlaskForm)

    # il n'y a pas encore de user_service_service ...
    usrSrv      = UserService()
    # usrSrv      = user_service_service.find_one(delivery.user_service_id)

    # il n'y a pas encore de user_service ...
    user        = User()
    # user        = user_service.find_one(usrSrv.rel_user)
    workername  = user.first_name + " " + user.last_name

    # il n'y a pas encore de service_service ...
    service     = Service()
    # service     = service_service.find_one(usrSrv.rel_service)
    servicename = service.name + " (" + service.service_type + ")"

    usrLst  = UserService.find_all()

    if delivery_id == -1:
        # add
        clId = -1
    else:
        # update
        clId = delivery.client_id

    return render_template('delivery/add_update.html',  form=frm,
                                                        clId=clId,
                                                        workername=workername,
                                                        servicename=servicename,
                                                        usrLst=usrLst)
