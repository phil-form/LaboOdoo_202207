from flask_wtf  import FlaskForm
from wtforms    import StringField, EmailField, IntegerField, SelectField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Regexp
from app.dtos.user_dto  import UserDTO

class UserRegisterform(FlaskForm):
    username    = StringField('username',   validators=[DataRequired()], default="")
    first_name  = StringField('first_name', validators=[DataRequired()], default="")
    last_name   = StringField('last_name',  validators=[DataRequired()], default="")
    mail        = EmailField('mail',        validators=[DataRequired(),
                                                        Regexp('[a-zA-Z](\w+\.?)*@[a-zA-Z]\w+\.[a-zA-Z]\w+(.[a-zA-Z]{1,4})*')], default="")
    password    = StringField('password',   validators=[DataRequired(), EqualTo('confirm'),
                                                        Regexp('^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{2,}$')], default="")
    confirm     = StringField('confirm',    validators=[DataRequired(), EqualTo('password')], default="")
    description = TextAreaField('description', default="")

    street      = StringField('street',     validators=[DataRequired()], default="")
    number      = IntegerField('number',    validators=[DataRequired()], default=0)
    zip_code    = IntegerField('zip_code',  validators=[DataRequired()], default=0)
    country     = SelectField('country',    validators=[DataRequired()], choices= [
                                                        "Belgium", "France", "England", "Germany", "Netherlands", "Italy", "Switzerland" ], default="")

    def get_as_userDTO(self):
        dto = UserDTO()
        dto.username        = self.username.data
        dto.firstname       = self.first_name.data
        dto.lastname        = self.last_name.data
        dto.mail            = self.mail.data
        dto.password        = self.password.data
        dto.description     = self.description.data
        dto.address.street  = self.street.data
        dto.address.number  = self.number.data
        dto.address.zip     = self.zip_code.data
        dto.address.country = self.country.data

        return dto

    def load_from_DTO(self, dto: UserDTO):
        self.username.data    = dto.username
        self.first_name.data  = dto.firstname
        self.last_name.data   = dto.lastname
        self.mail.data        = dto.mail
        self.password.data    = dto.password
        self.description.data = dto.description
        self.street.data      = dto.address.street
        self.number.data      = dto.address.number
        self.zip_code.data    = dto.address.zip
        self.country.data     = dto.address.country

        return self

    def get_attributes(self):
        return {
        "username":     self.username.data,
        "firstname":    self.first_name.data,
        "lastname":     self.last_name.data,
        "mail":         self.mail.data,
        "description":  self.description.data,
        "street":       self.street.data,
        "number":       self.number.data,
        "zip_code":     self.zip_code.data,
        "country":      self.country.data,
        }