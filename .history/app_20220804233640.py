from flask import Flask, render_template
from flask_bootstrap import Bootstrap 
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['']
db = SQLAlchemy(app)

app.config.from_object(Config)
@app.route("/")
def index():
    title = 'TodoList App'
    return render_template('index.html',title=title)
if __name__ == '__main__':
    app.run(debug=True)