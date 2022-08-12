from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    title = 'TodoList App'
    return render_template('index.html',title=title)

    