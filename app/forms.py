from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SendMessageForm(FlaskForm):
    message = StringField(validators=[DataRequired()], id="input_field")
    send = SubmitField('Send', id="send_button")