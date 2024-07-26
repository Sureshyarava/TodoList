import json

from behave import given, when, then
import requests

uri = "http://127.0.0.1:5000"


@given('user registers with given name "{name}" and email "{email}"')
def get_user(context, name, email):
    context.name = name
    context.email = email



@when('user is created with given name and email')
def user_tries_to_create_with_details(context):
    payload = {"name": context.name, "email": context.email}
    context.response = requests.post(uri + "/create_user", json=payload)


@then('user validates user is created sucessfully')
def user_validates_the_response(context):
    if context.response.status_code==200:
        data = context.response.json()
        assert data["message"] == "User created Successfully"
    else:
        print(context.response.text)

