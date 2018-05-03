from flask_wtf import Form
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, NumberRange


class AddEventForm(Form):
    event_prefix = IntegerField('Prefixo', validators=[NumberRange(), DataRequired()])
    event_xvm = StringField('XVM', validators=[DataRequired()])
