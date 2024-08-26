from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class ChatbotForm(FlaskForm):
    # User input is required for the bot to run.
    user_input = StringField('User Input', validators=[DataRequired()])
    submit = SubmitField('Send')
    