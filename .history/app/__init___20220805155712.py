from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
from flask_bootstrap import Bootstrap 
from config import Config
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
db.create_all()
bcrypt = Bcrypt(app)
app.config.from_object(Config)


from app.routes import *
'''def db_connection():
    conn = None
    try:
        conn = sqlite3.connect("todos.sqlite")
    except sqlite3.error as e:
        print(e)
    return conn
'''

