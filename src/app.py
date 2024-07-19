from flask import Flask, json, request, session
from .model import Schema
from .services import TodoService
import os

app = Flask(__name__)
random = os.urandom(12).hex()
app.config['SECRET_KEY'] = random


@app.route("/create_user", methods=["POST"])
def create_user():
    data = request.json
    response = TodoService().create_user(data["name"], data["email"])
    return json.jsonify({"message": response})


@app.route("/login", methods=["POST"])
def login():
    data = request.json
    response, statuscode = TodoService().login(data["email"])
    if statuscode == 200:
        session["user"] = response
        return json.jsonify({"message": "Login successful"})
    return json.jsonify({"message": response})


@app.route("/logout", methods=["POST"])
def logout():
    if "user" not in session:
        return json.jsonify({"message": "Please Login first to logout"})
    session.pop("user", None)
    return json.jsonify({"message": "Successfully Logged out"})


@app.route("/get_users")
def get_users():
    response = TodoService().get_users()
    return json.jsonify(response)


@app.route("/create_todo_item", methods=["POST"])
def create_todo_item():
    if "user" not in session:
        return json.jsonify({"message": "Please login to create a todo item"})
    data = request.json
    response = TodoService().create_new_todo(data["title"], data["description"], session["user"])
    return json.jsonify({"message": response})


@app.route("/update_title", methods=["PUT"])
def update_title():
    if "user" not in session:
        return json.jsonify({"message": "Please login to update"})
    data = request.json
    response = TodoService().update_title(data["title"], data["id"], session["user"])
    return json.jsonify({"message": response})

@app.route("/get_todoList")
def get_todoList():
    if "user" not in session:
        return json.jsonify({"message": "Please login to get the list of todos"})
    response = TodoService().get_todoList(session["user"])
    return json.jsonify({"todo_list": response})


if __name__ == "main":
    Schema()
    app.run(debug=True)
