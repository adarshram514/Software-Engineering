import sys 
sys.dont_write_bytecode = True
#Need to do the following installs:
# pip install flask-wtf
# pip install email_validator
from flask_wtf import Form
from wtforms import TextAreaField, SubmitField, validators, ValidationError

class AskmeForm(Form):
    prompt = TextAreaField("Your Question",  [validators.InputRequired("Please enter a question.")])
    submit = SubmitField("Send") 