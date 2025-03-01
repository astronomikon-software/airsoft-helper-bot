import psycopg2
from psycopg2 import OperationalError


class DbProvider:

    def __init__(
            self,
            database: str,
            user: str,
            password: str,
            host: str,
            port: int,
            autocommit=True
        ):
        self.connection = psycopg2.connect(
            dbname=database,
            user=user,
            password=password,
            host=host,
            port=port,
        )
        self.autocommit = autocommit
    
    def execute_query(self, query, values=set()):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, values)
            if self.autocommit == True:
                self.connection.commit()
        except OperationalError as e:
            self.connection.rollback()
            print(e)
        finally:
            cursor.close()
            if not self.connection.closed:
                self.connection.rollback()

    def execute_read_query(self, query, values=set()) -> list:
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, values)
            result = cursor.fetchall()
            return result
        except OperationalError as e:
            self.connection.rollback()
            print(e)
        finally:
            cursor.close()
            if not self.connection.closed:
                self.connection.rollback() # copied from the function above
    
    def begin(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute('''BEGIN;''')
        except OperationalError as e:
            print(e)

    def rollback(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute('''ROLLBACK;''')
        except OperationalError as e:
            print(e)
