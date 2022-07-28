from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length

class CommentAddForm(FlaskForm):
    content = StringField('content', validators=[DataRequired(), Length(1, 500)])