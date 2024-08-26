from flask import Flask


app = Flask(__name__)

app.secret_key = 'development key'
app.config['SECRET_KEY']='LongAndRandomSecretKey'

#mail.init_app(app)
from .routes import mail

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://your-username:your-password@localhost/development'
from models import db
db.init_app(app)
mail.init_app(app)