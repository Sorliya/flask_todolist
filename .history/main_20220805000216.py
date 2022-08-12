from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/jiangzihui/Downloads/flask/microblog/example.db'
db = SQLAlchemy(app)

class ExampleTable(db.Model):
    id=db.Column(db.Integer, primary_key=True)