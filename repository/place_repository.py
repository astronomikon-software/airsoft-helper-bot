from model.place import Place
from data.db_provider import DbProvider
from mapping.place_mapping import place_from_row
from utils.list_util import place_from_name_row


class PlaceRepository:

    def __init__(self, db_provider: DbProvider):
        self.db_provider = db_provider
    
    def read_all(self) -> list[Place]:
        row = self.db_provider.execute_read_query('''SELECT DISTINCT place_name FROM matches;''')
        return list(map(place_from_name_row, row))

    def read_by_id(self, id: int) -> Place:
        rows = self.db_provider.execute_read_query(
            '''SELECT * FROM places WHERE id = %s''',
            (id,)
        )
        return place_from_row(rows[0])
