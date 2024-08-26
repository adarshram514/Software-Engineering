import sys 
sys.dont_write_bytecode = True
#Need to do the following installs:
# pip install flask-wtf
# pip install email_validator
from flask_wtf import Form
from wtforms import TextAreaField, SubmitField, validators, ValidationError
from openai import OpenAI

class Speechme(Form):
    prompt = TextAreaField("Enter your text to speech.",  [validators.InputRequired("Write your prompt.")])
    submit = SubmitField("Submit")