#Need to do the following installs:
# pip install flask-wtf
# pip install email_validator
from flask_wtf import Form, FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, validators, ValidationError
from models import db, User

class ContactForm(Form):
    name = StringField("Name",  [validators.InputRequired("Please enter your name.")])
    email = StringField("Email",  [validators.InputRequired("Please enter your email address."), validators.Email("Please enter your email address.")])
    subject = StringField("Subject",  [validators.InputRequired("Please enter a subject.")])
    message = TextAreaField("Message",  [validators.InputRequired("Please enter a message.")])
    submit = SubmitField("Send") 
class SignupForm(Form):
  firstname = TextField("First name",  [validators.Required("Please enter your first name.")])
  lastname = TextField("Last name",  [validators.Required("Please enter your last name.")])
  email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
  password = PasswordField('Password', [validators.Required("Please enter a password.")])
  submit = SubmitField("Create account")
  def __init__(self, *args, **kwargs):
    Form.__init__(self, *args, **kwargs)


  def validate(self):
    if not Form.validate(self):
      return False
    
    user = User.query.filter_by(email = self.email.data.lower()).first()
    if user:
      self.email.errors.append("That email is already taken")
      return False
    else:
      return True

class SigninForm(Form):
  email = TextField("Email",  [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
  password = PasswordField('Password', [validators.Required("Please enter a password.")])
  submit = SubmitField("Sign In")
  
  def __init__(self, *args, **kwargs):
    Form.__init__(self, *args, **kwargs)

  def validate(self):
    if not Form.validate(self):
      return False
    
    user = User.query.filter_by(email = self.email.data).first()
    if user and user.check_password(self.password.data):
      return True
    else:
      self.email.errors.append("Invalid e-mail or password")
      return False
