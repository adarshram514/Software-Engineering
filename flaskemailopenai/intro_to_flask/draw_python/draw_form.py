import sys 
sys.dont_write_bytecode = True
#Need to do the following installs:
# pip install flask-wtf
# pip install email_validator
from flask_wtf import Form
from wtforms import SelectField, TextAreaField, SubmitField, validators, ValidationError

class DrawmeForm(Form):
    prompt = TextAreaField("What would you like to draw?",  [validators.InputRequired("Please enter a prompt.")])
    image_quality = SelectField("Image Quality", choices=[('standard', 'Standard'), ('hd', 'HD')])
    image_size = SelectField("Image Size", choices=[('1024x1024', '1024x1024'), ('1792x1024', '1792x1024')])
    submit = SubmitField("Send") 