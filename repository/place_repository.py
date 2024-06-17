from model.place import Place
from data.read_all_execution import execute_read_query
from mapping.place_mapping import place_from_row


class PlaceRepository:
    
    def read_all() -> list[Place]:
        rows = execute_read_query('''SELECT * from places''')
        return list(map(place_from_row, rows))
