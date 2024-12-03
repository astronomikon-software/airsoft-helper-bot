from data.db_provider import DbProvider
from model.duration import Duration
from mapping.duration_mapping import *


class DurationRepository:

    def __init__(self, db_provider: DbProvider):
        self.db_provider = db_provider
    
    def read_all(self) -> list[Duration]:
        rows = self.db_provider.execute_read_query('''SELECT * from durations;''')
        return list(map(duration_from_row, rows))
    
    def read_by_id(self, id: int) -> Duration:
        rows = self.db_provider.execute_read_query(
            '''SELECT * FROM durations WHERE id = %s''',
            (id,)
        )
        return duration_from_row(rows[0])