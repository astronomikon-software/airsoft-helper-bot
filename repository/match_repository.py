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
        return list(map(match_from_row, rows)) # TODO

    def read_by_group(self, group_id: int, start_index: int, end_index: int) -> list[Match]:
        rows = self.db_provider.execute_read_query(
            '''SELECT * from matches WHERE group_id = %s''',
            (group_id,)
        )
        matches = list(map(match_from_row, rows))
        matches_from_now_on = list(filter(lambda match: match.start_time > datetime.datetime.now().timestamp(), matches))
        matches_from_now_on.sort(key=lambda match: match.start_time)
        return matches_from_now_on[start_index:end_index]

    def read_by_loneliness(self, loneliness_status, start_index: int, end_index: int) -> list[Match]:
        rows = self.db_provider.execute_read_query(
            '''SELECT * from matches WHERE is_loneliness_friendly is %s''',
            (loneliness_status,)
        )
        matches = list(map(match_from_row, rows))
        matches_from_now_on = list(filter(lambda match: match.start_time > datetime.datetime.now().timestamp(), matches))
        matches_from_now_on.sort(key=lambda match: match.start_time)
        return matches_from_now_on[start_index:end_index]
    
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
