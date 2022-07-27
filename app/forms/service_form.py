from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, RadioField, TextAreaField
from wtforms.validators import DataRequired

from app import app
from app.services.service_type_service import ServiceTypeService


class ServiceForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()], default='')
    request = RadioField('request', validators=[DataRequired()])
    service_type = SelectField('service_type', validators=[DataRequired()])
    description = TextAreaField('description', default='')

    def __init__(self, *args, **kwargs):
        super(ServiceForm, self).__init__(*args, **kwargs)
        self.request.choices = ['request', 'offer']
        service_type_service = app.injector[ServiceTypeService.__name__]
        self.service_type.choices = [service_type.name for service_type in service_type_service.find_all()]
