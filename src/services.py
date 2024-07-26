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
            response.append({"name": i[0], "email": i[1], "id": i[2]})
        return response

    def create_new_todo(self, title, description, createdBy):
        params = {"title": title, "description": description, "createdBy": createdBy}
        return self.db.create_todo_item(params)

    def get_todoList(self, user):
        result = self.db.get_todo_list(user)
        response = []
        for row in result:
            dictionary = {
                "id": row[0],
                "title": row[1],
                "description": row[2]
            }
            response.append(dictionary)
        return response

    def login(self, email):
        result = self.db.login(email)
        if result and email in result[0]:
            return result[0][2], 200
        return "Please sign in or recheck email_id you have entered", 400

    def update(self, params):
        result = self.db.update(params["title"], params["description"], params["id"], params["user"])
        return result

    def delete(self, id, user):
        result = self.db.delete(id, user)
        return result

    def delete_user(self, id):
        result, statuscode = self.db.delete_user(id)
        return result, statuscode