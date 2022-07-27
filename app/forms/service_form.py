from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, RadioField, TextAreaField
from wtforms.validators import DataRequired

from app.services.service_type_service import ServiceTypeService


class ServiceForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    request = RadioField('request', validators=[DataRequired()])
    service_type = SelectField('service_type', validators=[DataRequired()])
    description = TextAreaField('description')

    def __init__(self, *args, **kwargs):
        super(ServiceForm, self).__init__(*args, **kwargs)
        service_type_service = ServiceTypeService()
        self.request.choices = ['request', 'offer']
        self.service_type.choices = [service_type.name for service_type in service_type_service.find_all()]
