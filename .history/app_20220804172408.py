from flask import Flask, render_template
from flask_bootstrap import Bootstrap 
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from config import Config

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

app.config.from_object(Config)
@app.route("/")
def index():
    title = 'TodoList App'
    return render_template('index.html',title=title)
if __name__ == '__main__':
    app.run(debug=True)