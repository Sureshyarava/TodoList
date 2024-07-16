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
                    EMAIL TEXT,
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
        except:
            raise Exception("Error while inserting into table User")

    def get_users(self):
        query = f"Select * from User;"
        self.cursor.execute(query)
        self.connection.commit()
        result = self.cursor.fetchall()
        for row in result:
            print(row)
