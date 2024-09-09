from model.match import Match
from model.genre import Genre
from model.group import Group
from model.place import Place
from data.db_provider import DbProvider
from mapping.match_mapping import match_from_row
from mapping.datetime_mapping import int_to_datetime


class MatchRepository:

    def __init__(self, db_provider: DbProvider):
        self.db_provider = db_provider

    def create(self, match: Match):
        start_time_obj = int_to_datetime(match.start_time)
        # duration_obj = int_to_datetime(match.duration)
        self.db_provider.execute_query(
            '''INSERT INTO matches (start_time, place_id, group_id, genre_id, is_loneliness_friendly) VALUES (%s, %s, %s, %s, %s)''',
            (
                start_time_obj,
                match.place_id,
                match.group_id,
                match.genre_id,
                match.is_loneliness_friendly
            )
        )
    
    def read(self, match_id: int) -> Match:
        row = self.db_provider.execute_read_query(
            '''SELECT * from matches WHERE id = %s''',
            (match_id,)
        )[0]
        return match_from_row(row)

    def update(self, match: Match):
        start_time_obj = int_to_datetime(match.start_time)
        # duration_obj = int_to_datetime(match.duration)
        self.db_provider.execute_query(
            '''UPDATE matches SET start_time = %s, duration = %s, place_id = %s, group_id = %s, genre_id = %s, is_loneliness_friendly = %s WHERE id = %s''',
            (
                start_time_obj,
                # duration_obj,
                match.place_id,
                match.group_id,
                match.genre_id,
                match.is_loneliness_friendly,
                match.id
            )
        )

    def delete(self, match: Match):
        self.db_provider.execute_query(
            '''DELETE FROM matches WHERE id = %s''',
            (match.id,)
        )

    def read_all(self) -> list[Match]:
        rows = self.db_provider.execute_read_query('''SELECT * from matches''')
        return list(map(match_from_row, rows))

    def read_by_genre(self, genre_id: int) -> list[Match]:
        rows = self.db_provider.execute_read_query(
            '''SELECT * from matches WHERE genre_id = %s''',
            (genre_id,)
        )
        return list(map(match_from_row, rows))

    def read_by_place(self, place_id: int) -> list[Match]:
        rows = self.db_provider.execute_read_query(
            '''SELECT * from matches WHERE place_id = %s''',
            (place_id,)
        )
        return list(map(match_from_row, rows))

    def read_by_group(self, group_id: int) -> list[Match]:
        rows = self.db_provider.execute_read_query(
            '''SELECT * from matches WHERE group_id = %s''',
            (group_id,)
        )
        return list(map(match_from_row, rows))

    def read_by_loneliness(self, loneliness_status) -> list[Match]:
        rows = self.db_provider.execute_read_query(
            '''SELECT * from matches WHERE is_loneliness_friendly is %s''',
            (loneliness_status,)
        )
        return list(map(match_from_row, rows))
