from .model import Schema


class TodoService:

    def __init__(self):
        self.db = Schema()

    def create_user(self, name, email):
        params = {"name": name, "email": email}
        return self.db.create_user(params)

    def get_users(self):
        result = self.db.get_users()
        response = []
        for i in result:
            response.append({"name" : i[0], "email" : i[1], "id" : i[2]})
        return response

    def create_new_todo(self, title, description, createdBy):
        params = {"title": title, "description": description, "createdBy": createdBy}
        return self.db.create_todo_item(params)

    def get_todoList(self):
        result = self.db.get_todo_list()
        response = []
        print(result)
        return result