from model.genre import Genre
from data.db_provider import DbProvider
from mapping.genre_mapping import genre_from_row


class GenreRepository:
        
    def __init__(self, db_provider: DbProvider):
        self.db_provider = db_provider
    
    def read_all(self) -> list[Genre]:
        rows = self.db_provider.execute_read_query('''SELECT * from genres''')
        return list(map(genre_from_row, rows))
