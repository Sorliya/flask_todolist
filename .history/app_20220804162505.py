from flask import Flask
from flask_bootstrap import Bootstrap 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


@app.route("/")
def index():
    
    return 'hello'
if __name__ == '__main__':
    app.run(debug=True)