from flask import Flask,request,session, jsonify
from .model import Schema
from .services import TodoService
import os
from functools import wraps

app = Flask(__name__)
random = os.urandom(12).hex()
app.config['SECRET_KEY'] = random


def is_user_logged_in(func):
    @wraps(func)  # This preserves the original function's metadata
    def wrapper(*args, **kwargs):
        if "user" not in session:
            return jsonify({"message": "Please login to proceed further"}), 401  # Return a 401 Unauthorized status
        return func(*args, **kwargs)  # Call the original function with unpacked arguments

    return wrapper


def is_admin(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "admin" in session:
            return func(*args, **kwargs)
        return jsonify({"message": "Don't try to fool me :) login with admin credentials"}), 401

    return wrapper


@app.route("/create_user", methods=["POST"])
def create_user():
    data = request.json
    response = TodoService().create_user(data["name"], data["email"])
    return jsonify({"message": response})


@app.route("/login", methods=["POST"])
def login():
    data = request.json
    response, statuscode = TodoService().login(data["email"])
    if statuscode == 200:
        if data["email"] == "admin":
            session["admin"] = response
        session["user"] = response
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"message": response}), 400


@app.route("/logout", methods=["POST"])
@is_user_logged_in
def logout():
    session.pop("user", None)
    session.clear()
    if "admin" in session:
        session.pop("admin", None)
    return jsonify({"message": "Successfully Logged out"}), 200


@app.route("/get_users")
@is_user_logged_in
def get_users():
    response = TodoService().get_users()
    return jsonify(response), 200


@app.route("/create_todo_item", methods=["POST"])
@is_user_logged_in
def create_todo_item():
    data = request.json
    response = TodoService().create_new_todo(data["title"], data["description"], session["user"])
    return jsonify({"message": response}), 200


@app.route("/update_todo_item", methods=["PUT"])
@is_user_logged_in
def update():
    data = request.json
    params = {"id": data["id"], "user": session["user"], "description": data.get("description", None),
              "title": data.get("title", None)}
    response = TodoService().update(params)
    return jsonify({"message": response})


@app.route("/delete_todo", methods=["PUT"])
@is_user_logged_in
def delete_todo_item():
    data = request.json
    response = TodoService().delete(data["id"], session["user"])
    return jsonify({"message": response}), 200


@app.route("/delete_user", methods=["DELETE"])
@is_user_logged_in
def delete_user():
    response, status = TodoService().delete_user(session["user"])
    if status == 200:
        logout()
        return jsonify({"message": response}), 200
    return jsonify({"message": response}), 400


@app.route("/get_todoList")
@is_user_logged_in
def get_todoList():
    response = TodoService().get_todoList(session["user"])
    return jsonify({"todo_list": response}), 200


if __name__ == "main":
    Schema()
    app.run(debug=True)
