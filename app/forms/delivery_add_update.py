import re

from flask_wtf                  import FlaskForm
from wtforms                    import IntegerField, StringField, DateField, BooleanField, SelectField
from wtforms.validators         import DataRequired, NumberRange

from app.services.user_service  import UserService

from app.models.user import User

class DeliveryAddUpdateForm(FlaskForm):
    clientname  = SelectField ('clientname'                              )
    startdate   = DateField   ('startdate'  , validators=[DataRequired()])
    duration    = StringField ('duration'   , validators=[DataRequired()])
    durationeff = StringField ('durationeff'                             )
    done        = BooleanField('done'                                    )

    def __init__(self, *args,**kwargs):
        super(DeliveryAddUpdateForm, self).__init__(*args, **kwargs)
        #self.usr_lst = UserService()
        #self.clientname.choices = [str(usr.user_id) for usr in self.usr_lst.find_all()]
        self.usr_lst = []                   # temporaire
        self.usr0 = User()                  # temporaire
        self.usr0.user_id = -1              # temporaire
        self.usr0.first_name = "Choisissez" # temporaire
        self.usr0.last_name = ""            # temporaire
        self.usr_lst.append(self.usr0)      # temporaire
        self.usr1 = User()                  # temporaire
        self.usr1.user_id = 2               # temporaire
        self.usr1.first_name = "Alfred"     # temporaire
        self.usr1.last_name = "Dupont"      # temporaire
        self.usr_lst.append(self.usr1)      # temporaire
        self.usr2 = User()                  # temporaire
        self.usr2.user_id = 3               # temporaire
        self.usr2.first_name = "Barnabé"    # temporaire
        self.usr2.last_name = "Martin"      # temporaire
        self.usr_lst.append(self.usr2)      # temporaire
        self.usr3 = User()                  # temporaire
        self.usr3.user_id = 4               # temporaire
        self.usr3.first_name = "Casimir"    # temporaire
        self.usr3.last_name = "Durand"      # temporaire
        self.usr_lst.append(self.usr3)      # temporaire
        self.clientname.choices = [str(usr.user_id) for usr in self.usr_lst]

    def validate_duration(form, field):
        if not re.search(r"^[0-9]+:[0-5][0-9]$", field.data):
            raise ValidationError("Format incorrect pour la durée: h:mm")

    def validate_duration_effective(form, field):
        if not re.search(r"^[0-9]+:[0-5][0-9]$", field.data):
            raise ValidationError("Format incorrect pour la durée: h:mm")
