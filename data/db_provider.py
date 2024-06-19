import psycopg2
from psycopg2 import OperationalError


class DbProvider:
    def __init__(self, database, user, password, host, port):
        self.connection = psycopg2.connect(
            database,
            user,
            password,
            host,
            port,
        )
    
    def execute_query(self, query, values=set()):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, values)
            self.connection.commit()
        except OperationalError as e:
            print(e)

    def execute_read_query(self, query, values=set()):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, values)
            result = cursor.fetchall()
            return result
        except OperationalError as e:
            print(e)