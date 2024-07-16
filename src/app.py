from flask import Flask
from .model import Schema
from .services import TodoService

app = Flask(__name__)


@app.route("/")
def hello_world():
    TodoService().create_user("name", "email")
    TodoService().get_users()
    return f'<h1>Hello name</h1>'


if __name__ == "main":
    Schema()
    app.run(debug=True)