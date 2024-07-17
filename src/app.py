from flask import Flask, json, request
from .model import Schema
from .services import TodoService

app = Flask(__name__)


@app.route("/create_user", methods=["POST"])
def create_user():
    data = request.json
    response = TodoService().create_user(data["name"], data["email"])
    return json.jsonify({"message": response})


@app.route("/get_users")
def get_users():
    response = TodoService().get_users()
    return json.jsonify(response)


@app.route("/create_todo_item", methods=["POST"])
def create_todo_item():
    data = request.json
    response = TodoService().create_new_todo(data["title"], data["description"], data["user"])
    return json.jsonify(response)


@app.route("/get_todoList")
def get_todoList():
    response = TodoService().get_todoList()
    return json.jsonify(response)


if __name__ == "main":
    Schema()
    app.run(debug=True)
