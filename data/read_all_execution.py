import psycopg2
from psycopg2 import OperationalError


def execute_read_query(connection, query, values=set()):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query, values)
        result = cursor.fetchall()
        return result
    except OperationalError as e:
        print(e)
