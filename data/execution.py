import psycopg2
from psycopg2 import OperationalError


def execute_query(connection, query, values):
    cursor = connection.cursor()
    try:
        cursor.execute(query, values)
        connection.commit()
    except OperationalError as e:
        print('Ошибка:', e)
     