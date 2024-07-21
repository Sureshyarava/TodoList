from behave import given, when, then


@given('user is having "{name}" , "{email}"')
def get_user(context, name, email):
    print("Inside given ",name, email)
    context.name = name
    context.email = email


@when('user is created with given name and email')
def user_tries_to_create_with_details(context):
    print("Inside when ", context.name, context.email)


@then('user gets a response saying user is successfully created')
def user_validates_the_response(context):
    print("inside then ", context.name, context.email)
