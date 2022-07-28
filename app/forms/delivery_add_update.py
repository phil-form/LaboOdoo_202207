import re

from flask_wtf                  import FlaskForm
from wtforms                    import IntegerField, StringField, DateField, BooleanField, SelectField
from wtforms.validators         import DataRequired, NumberRange

from app.services.user_service  import UserService

class DeliveryAddUpdateForm(FlaskForm):
    clientname  = SelectField ('clientname'                              )
    startdate   = DateField   ('startdate'  , validators=[DataRequired()])
    duration    = StringField ('duration'   , validators=[DataRequired()])
    durationeff = StringField ('durationeff'                             )
    done        = BooleanField('done'                                    )

    def __init__(self, *args,**kwargs):
        super(DeliveryAddUpdateForm, self).__init__(*args, **kwargs)
        self.usr_lst = UserService()
        self.clientname.choices = [str(usr.user_id) for usr in self.usr_lst.find_all()]

    def validate_duration(form, field):
        if not re.search(r"^[0-9]+:[0-5][0-9]$", field.data):
            raise ValidationError("Format incorrect pour la durée: h:mm")

    def validate_duration_effective(form, field):
        if not re.search(r"^[0-9]+:[0-5][0-9]$", field.data):
            raise ValidationError("Format incorrect pour la durée: h:mm")
