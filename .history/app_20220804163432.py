from flask import Flask
from flask_bootstrap import Bootstrap 
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

@app.route("/")
def index():
    title = 'TodoList App'
    return render_template('index.html',title=title)
if __name__ == '__main__':
    app.run(debug=True)