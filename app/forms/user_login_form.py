from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from app.models.user import User
from app.dtos.user_dto import UserDTO

class UserLoginform(FlaskForm):
    login = StringField('login', validators=[DataRequired()], default="")
    password = StringField('password', validators=[DataRequired()], default="")