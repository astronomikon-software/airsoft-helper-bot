import datetime
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
        self.db_provider.execute_query(
            '''INSERT INTO matches (start_time, place_id, group_id, genre_id, is_loneliness_friendly, last_edit_time) VALUES (%s, %s, %s, %s, %s, NOW())''',
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
        self.db_provider.execute_query(
            '''UPDATE matches SET start_time = %s, place_id = %s, group_id = %s, genre_id = %s, is_loneliness_friendly = %s, last_edit_time = NOW() WHERE id = %s''',
            (
                start_time_obj,
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

    def read_by_genre(self, genre_id: int, limit: int, offset: int) -> list[Match]:
        rows = self.db_provider.execute_read_query(
            '''SELECT * from matches WHERE start_time > NOW() AND genre_id = %s ORDER BY start_time LIMIT %s OFFSET %s;''',
            (
                genre_id,
                limit,
                offset,
            )
        )
        return list(map(match_from_row, rows))
    
    def count_by_genre(self, genre_id: int) -> int:
        number = self.db_provider.execute_read_query(
            '''SELECT COUNT(*) FROM matches WHERE start_time > NOW() AND genre_id = %s;''',
            (genre_id,)
        )[0][0]
        return number

    def read_by_place(self, place_id: int, limit: int, offset: int) -> list[Match]:
        rows = self.db_provider.execute_read_query(
            '''SELECT * from matches WHERE start_time > NOW() AND place_id = %s ORDER BY start_time LIMIT %s OFFSET %s;''',
            (
                place_id,
                limit,
                offset,
            )
        )
        return list(map(match_from_row, rows))
    
    def count_by_place(self, place_id: int) -> int:
        number = self.db_provider.execute_read_query(
            '''SELECT COUNT(*) FROM matches WHERE start_time > NOW() AND place_id = %s;''',
            (place_id,)
        )[0][0]
        return number


    def read_by_group(self, group_id: int, limit: int, offset: int) -> list[Match]:
        rows = self.db_provider.execute_read_query(
            '''SELECT * from matches WHERE start_time > NOW() AND group_id = %s ORDER BY start_time LIMIT %s OFFSET %s;''',
            (
                group_id,
                limit,
                offset,
            )
        )
        return list(map(match_from_row, rows))
    
    def count_by_group(self, group_id: int) -> int:
        number = self.db_provider.execute_read_query(
            '''SELECT COUNT(*) FROM matches WHERE start_time > NOW() AND group_id = %s;''',
            (group_id,)
        )[0][0]
        return number

    def read_by_loneliness(self, loneliness_status, limit: int, offset: int) -> list[Match]:
        rows = self.db_provider.execute_read_query(
            '''SELECT * from matches WHERE start_time > NOW() AND is_loneliness_friendly is %s ORDER BY start_time LIMIT %s OFFSET %s;''',
            (
                loneliness_status,
                limit,
                offset,
            )
        )
        return list(map(match_from_row, rows))
    
    def count_by_loneliness(self, loneliness_status) -> int:
        number = self.db_provider.execute_read_query(
            '''SELECT COUNT(*) FROM matches WHERE start_time > NOW() AND is_loneliness_friendly is %s;''',
            (loneliness_status,)
        )[0][0]
        return number
    
    def read_ongoing(self, limit: int, offset: int) -> list[Match]:
        rows = self.db_provider.execute_read_query(
            '''SELECT * FROM matches WHERE start_time > NOW() ORDER BY start_time LIMIT %s OFFSET %s;''',
            (limit, offset,)
        )        
        return list(map(match_from_row, rows))
    
    def count_all_ongoings(self) -> int:
        number_of_ongoings = self.db_provider.execute_read_query(
            '''SELECT COUNT(*) FROM matches WHERE start_time > NOW();'''
        )[0][0]
        return number_of_ongoings
    
    def read_by_updating(self, limit: int, offset: int) -> list[Match]:
        rows = self.db_provider.execute_read_query(
            '''SELECT * FROM matches ORDER BY last_edit_time DESC LIMIT %s OFFSET %s;''',
            (limit, offset,)
        )
        return list(map(match_from_row, rows))
    
    def count_all(self) -> int:
        number = self.db_provider.execute_read_query(
            '''SELECT COUNT(*) FROM matches;'''
        )[0][0]
        return number
