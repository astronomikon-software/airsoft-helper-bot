from model.genre import Genre
from data.read_all_execution import execute_read_query
from mapping.genre_mapping import genre_from_row


class GenreRepository:
    
    def read_all():
        rows = execute_read_query('''SELECT * from genres''')
        return list(map(genre_from_row, rows))
