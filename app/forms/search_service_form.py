from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired


class SearchServiceForm(FlaskForm):
    search_content = StringField('search_content', default='')
    search_target = SelectField('search_target', validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        super(SearchServiceForm, self).__init__(*args, **kwargs)
        self.search_target.choices = ['All', 'Name', 'Description', 'User', 'Type', 'Request', 'Offer']
