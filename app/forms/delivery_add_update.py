import re

from flask_wtf                  import FlaskForm
from wtforms                    import StringField, DateField, BooleanField, SelectField

from app.services.user_service  import UserService
from app.models.user            import User
from app.dtos.user_dto          import UserDTO

class DeliveryAddUpdateForm(FlaskForm):
    usrsrv      = StringField ('usrsrv'     )
    clientname  = SelectField ('clientname' )
    startdate   = DateField   ('startdate'  )
    duration    = StringField ('duration'   )
    durationeff = StringField ('durationeff')
    dur_str     = StringField ('dur_str'    )
    eff_str     = StringField ('eff_str'    )
    done        = BooleanField('done'       )

    def __init__(self, *args,**kwargs):
        super(DeliveryAddUpdateForm, self).__init__(*args, **kwargs)
        self.usr_lst = UserService()
        self.clientname.choices = [str(usr.user_id) for usr in self.usr_lst.find_all()]

    def validate_dur_str(form, field):
        if not re.search(r"^[0-9]+:[0-5][0-9]$", field.data):
            raise ValidationError("Format incorrect pour la durée: h:mm")

    def validate_eff_str(form, field):
        if not re.search(r"^[0-9]+:[0-5][0-9]$", field.data):
            raise ValidationError("Format incorrect pour la durée: h:mm")
