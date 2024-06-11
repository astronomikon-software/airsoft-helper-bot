import psycopg2
from psycopg2 import OperationalError

from connection import connection


def execute_query(query, values=set()):
    cursor = connection.cursor()
    try:
        cursor.execute(query, values)
        connection.commit()
    except OperationalError as e:
        print(e)
     