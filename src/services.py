from .model import Schema


class TodoService:

    def __init__(self):
        self.db = Schema()

    def create_user(self, name, email):
        params = {"name": name, "email": email}
        self.db.create_user(params)

    def get_users(self):
        self.db.get_users()