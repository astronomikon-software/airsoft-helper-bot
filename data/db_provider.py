import psycopg2
from psycopg2 import OperationalError


class DbProvider:
    def __init__(self, database, user, password):
        self.connection = psycopg2.connect(f'dbname={database} user={user} password={password}')
    
    def execute_query(self, query, values=set()):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, values)
            self.connection.commit()
        except OperationalError as e:
            print(e)

    def execute_read_query(self, query, values=set()) -> list:
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, values)
            result = cursor.fetchall()
            return result
        except OperationalError as e:
            print(e)