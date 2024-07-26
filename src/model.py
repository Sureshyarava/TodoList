import sqlite3
from pprint import pprint


class Schema:
    def __init__(self):
        self.connection = sqlite3.connect("todo.db")
        self.cursor = self.connection.cursor()
        self.create_user_table()
        self.create_todo_list_table()

    def create_todo_list_table(self):
        try:
            query = """
                CREATE TABLE IF NOT EXISTS "Todo" (
                ID Integer Primary Key AUTOINCREMENT,
                TITLE varchar(25),
                DESCRIPTION MEDIUMTEXT,
                CreatedOn DATETIME,
                UpdatedOn DATETIME,
                Is_Deleted Boolean,
                CreatedBy Integer,
                Foreign Key(CreatedBy) References User(ID)
                );
                """
            self.cursor.execute(query)
            self.connection.commit()
        except:
            raise Exception("Error while creating table todoList")

    def create_user_table(self):
        try:
            query = """
                    CREATE TABLE IF NOT EXISTS "User" (
                    NAME varchar(50),
                    EMAIL TEXT UNIQUE,
                    ID Integer Primary Key AUTOINCREMENT
                    );
                    """
            self.cursor.execute(query)
            self.connection.commit()
        except:
            raise Exception("Error while creating User Table")

    def create_user(self, params):
        try:
            query = f" INSERT into USER \
                    (NAME, EMAIL) Values \
                    ('{params['name']}', '{params['email']}') ;\
                    "
            print(query)
            self.cursor.execute(query)
            self.connection.commit()
            return "User created Successfully"
        except sqlite3.IntegrityError:
            return "Email Id is already present. Please Login"

    def get_users(self):
        query = f"Select * from User;"
        self.cursor.execute(query)
        self.connection.commit()
        result = self.cursor.fetchall()
        # for row in result:
        #     print(row)
        return result

    def create_todo_item(self, params):
        try:
            query = f" INSERT INTO Todo \
                    (TITLE, DESCRIPTION, CreatedOn, UpdatedOn, Is_Deleted, CreatedBy) Values \
                    ('{params['title']}', '{params['description']}', datetime('now'),  datetime('now'), FALSE, '{params['createdBy']}');"
            self.cursor.execute(query)
            self.connection.commit()
            return "Todo Item successfully created"
        except Exception:
            raise Exception("Error while inserting into table")

    def get_todo_list(self, user):
        try:
            query = f"Select * from todo where createdBy = {user} and Is_Deleted = FALSE order by updatedOn desc "
            self.cursor.execute(query)
            self.connection.commit()
            result = self.cursor.fetchall()
            return result
        except:
            raise Exception("Error in fetching Todo list")

    def login(self, email):
        try:
            query = f"select * from user where email = '{email}'"
            self.cursor.execute(query)
            self.connection.commit()
            result = self.cursor.fetchall()
            return result
        except:
            raise Exception("Error while fetching email")

    def update(self, title, description, id, user):
        try:
            query = ""
            if description and title:
                query = (f"Update todo set title = '{title}', description='{description}', UpdatedOn = datetime('now') \
                         where id = {id} and createdBy = {user}")
            elif description:
                query = (f"Update todo set description='{description}', UpdatedOn = datetime('now') \
                                         where id = {id} and createdBy = {user}")
            else:
                query = (f"Update todo set title = '{title}', UpdatedOn = datetime('now') \
                                         where id = {id} and createdBy = {user}")
            self.cursor.execute(query)
            self.connection.commit()
            return "Successful"
        except Exception as e:
            print("error is ",e)
            return "Error while updating"

    def delete(self, id, user):
        try:
            query = f"update  todo set Is_Deleted=TRUE where id = {id} and createdBy = {user}"
            self.cursor.execute(query)
            self.connection.commit()
            return "deleted successfully"
        except Exception as e:
            print("Error while deleting a todo item")
            return "error while deleting"

    def delete_user(self, id):
        try:
            query = "Delete from user where id = ?"
            self.cursor.execute(query,[id])
            self.connection.commit()
            return "User deleted Successfully" , 200
        except Exception as e:
            print(e)
            return "Error while deleting User" , 400
