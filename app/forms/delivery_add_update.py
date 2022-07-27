import re

from flask_wtf          import FlaskForm
from wtforms            import IntegerField, StringField, DateField, BooleanField
from wtforms.validators import DataRequired

class DeliveryAddUpdateForm(FlaskForm):
    client_str  = StringField ('clientname' , validators=[DataRequired()])
    start_date  = DateField   ('startdate'  , validators=[DataRequired()])
    dur_str     = StringField ('duration'   , validators=[DataRequired()])
    dur_eff_str = StringField ('durationeff'                             )
    done        = BooleanField('done'                                    )

    def validate_duration(form, field):
        if not re.search(r"^[0-9]+:[0-5][0-9]$", field.data):
            raise ValidationError("Format incorrect pour la durée: h:mm")

    def validate_duration_effective(form, field):
        if not re.search(r"^[0-9]+:[0-5][0-9]$", field.data):
            raise ValidationError("Format incorrect pour la durée: h:mm")
