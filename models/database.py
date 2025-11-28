import sqlite3
from datetime import datetime

class Db_sqlite:
    def __init__(self, db_path):
        self.db_path = db_path
        self.__conection = sqlite3.connect(self.db_path)
        self.__cursor = self.__conection.cursor()
        self.tables_create()

    def tables_create(self):
        
        self.__cursor.execute("""CREATE TABLE IF NOT EXISTS income (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL UNIQUE,
                    value FLOAT NOT NULL,
                    created DATETIME DEFAULT CURRENT_TIMESTAMP
                    )""")

        self.__cursor.execute("""CREATE TABLE IF NOT EXISTS outcome (
                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            title TEXT NOT NULL,
                            value FLOAT NOT NULL,
                            created DATETIME DEFAULT CURRENT_TIMESTAMP
                            )""")
        
        self.__cursor.execute("""CREATE TABLE IF NOT EXISTS bills (
                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            title TEXT NOT NULL,
                            value FLOAT NOT NULL,
                            created DATETIME DEFAULT CURRENT_TIMESTAMP
                            )""")
        
        self.__cursor.execute("""CREATE TABLE IF NOT EXISTS investment (
                            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                            title TEXT NOT NULL,
                            value FLOAT NOT NULL,
                            created DATETIME DEFAULT CURRENT_TIMESTAMP
                            )""")
        
        self.__conection.commit()

    def insert(self, table_name, value_title, value):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        query = f"""INSERT INTO {table_name} (title, value, created) VALUES (?, ?, ?)"""
        try:
            self.__cursor.execute(query, (value_title, value, now))
            self.__conection.commit()
        except Exception as e:
            print(f"[WARNING] {e}")
            return None

    def select_all(self, table_name):
        query = f"""SELECT * FROM {table_name}"""

        try:
            self.__cursor.execute(query)
            dataset = self.__cursor.fetchall()
            self.__conection.commit()

            for data in dataset:
                id, title, value, created = data
                print(f"""Id: {id}\n    Title: {title}\n    Value: {value}\n    Created: {created}\n""")

            return data
        
        except Exception as e:
            print(f"[Warning] {e}")
            return None
