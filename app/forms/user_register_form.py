from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, IntegerField, SelectField
from wtforms.validators import DataRequired, EqualTo, Regexp
from app.models.user import User
from app.dtos.user_dto import UserDTO

class UserRegisterform(FlaskForm):
    username = StringField('username', validators=[DataRequired()], default="")
    first_name = StringField('first_name', validators=[DataRequired()], default="")
    last_name = StringField('last_name', validators=[DataRequired()], default="")
    mail = EmailField('mail', validators=[DataRequired(), Regexp('[a-zA-Z](\w+\.?)*@[a-zA-Z]\w+\.[a-zA-Z]\w+(.[a-zA-Z]{1,4})*')], default="")
    password = StringField('password', validators=[DataRequired(), EqualTo('confirm')], default="")
    #Regexp('^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{2,}$')
    confirm = StringField('confirm', validators=[DataRequired(), EqualTo('password')], default="")

    street = StringField('street', validators=[DataRequired()], default="")
    number = IntegerField('number', validators=[DataRequired()], default=0)
    zip_code = IntegerField('zip_code', validators=[DataRequired()], default=0)
    country = SelectField('country', validators=[DataRequired()], choices= [
        "Belgium", "France", "England", "Germany", "Netherlands", "Italy", "Switzerland" ], default="")

    def get_as_userDTO(self):
        dto = UserDTO()
        dto.username = self.username.data
        dto.firstname = self.first_name.data
        dto.lastname = self.last_name.data
        dto.mail = self.mail.data
        dto.password = self.password.data
        dto.address.street = self.street.data
        dto.address.number = self.number.data
        dto.address.zip = self.zip_code.data
        dto.address.country = self.country.data

        return dto
