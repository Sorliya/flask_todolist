from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
from flask_bootstrap import Bootstrap 
from config import Config
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
db.create_all()
bcrypt = Bcrypt(app)
mail = Mail(app)
login = LoginManager(app)
login.login_view = 'login'
login.login_message = 'You must login to access this page'
login.login_message_category = 'info'


from app.routes import *

