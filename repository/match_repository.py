import datetime
from typing import Callable
from model.match import Match
from data.db_provider import DbProvider
from mapping.match_mapping import match_from_row
from mapping.datetime_mapping import int_to_datetime


class MatchRepository:

    _on_match_created: Callable[[Match], None] = lambda _: None

    def __init__(self, db_provider: DbProvider):
        self.db_provider = db_provider

    def create(self, match: Match):
        start_time_obj = int_to_datetime(match.start_time)
        self.db_provider.execute_query(
            '''INSERT INTO matches (match_name, start_time, duration_id, place_name, group_id, genre_id, is_loneliness_friendly, url, annotation, last_edit_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, NOW())''',
            (
                match.name,
                start_time_obj,
                match.duration_id,
                match.place_name,
                match.group_id,
                match.genre_id,
                match.is_loneliness_friendly,
                match.url,
                match.annotation
            )
        )
        self._on_match_created(match)
    
    def read(self, match_id: int) -> Match:
        row = self.db_provider.execute_read_query(
            '''SELECT * from matches WHERE id = %s''',
            (match_id,)
        )[0]
        return match_from_row(row)

    def update(self, match: Match):
        start_time_obj = int_to_datetime(match.start_time)
        self.db_provider.execute_query(
            '''UPDATE matches SET match_name = %s, start_time = %s, duration_id = %s, place_name = %s, group_id = %s, genre_id = %s, is_loneliness_friendly = %s, url = %s, annotation = %s, last_edit_time = NOW() WHERE id = %s''',
            (
                match.name,
                start_time_obj,
                match.duration_id,
                match.place_name,
                match.group_id,
                match.genre_id,
                match.is_loneliness_friendly,
                match.url,
                match.annotation,
                match.id,
            )
        )

    def delete(self, match: Match):
        self.db_provider.execute_query(
            '''DELETE FROM matches WHERE id = %s''',
            (match.id,)
        )

    def read_by_duration(self, duration_id: int, limit: int, offset: int) -> list[Match]:
        rows = self.db_provider.execute_read_query(
            '''SELECT * from matches WHERE start_time > NOW() AND duration_id = %s ORDER BY start_time LIMIT %s OFFSET %s;''',
            (
                duration_id,
                limit,
                offset,
            )
        )
        return list(map(match_from_row, rows))
    
    def count_by_duration(self, duration_id: int) -> int:
        number = self.db_provider.execute_read_query(
            '''SELECT COUNT(*) FROM matches WHERE start_time > NOW() AND duration_id = %s;''',
            (duration_id,)
        )[0][0]
        return number

    def read_by_genre(self, genre_id: int, limit: int, offset: int) -> list[Match]:
        rows = self.db_provider.execute_read_query(
            '''SELECT * from matches WHERE start_time > NOW() AND %s = ANY (genre_id) ORDER BY start_time LIMIT %s OFFSET %s;''',
            (
                genre_id,
                limit,
                offset,
            )
        )
        return list(map(match_from_row, rows))
    
    def count_by_genre(self, genre_id: int) -> int:
        number = self.db_provider.execute_read_query(
            '''SELECT COUNT(*) FROM matches WHERE start_time > NOW() AND %s = ANY (genre_id);''',
            (genre_id,)
        )[0][0]
        return number

    def read_by_place(self, place_name: str, limit: int, offset: int) -> list[Match]:
        rows = self.db_provider.execute_read_query(
            '''SELECT * from matches WHERE start_time > NOW() AND place_name = %s ORDER BY start_time LIMIT %s OFFSET %s;''',
            (
                place_name,
                limit,
                offset,
            )
        )
        return list(map(match_from_row, rows))
    
    def count_by_place(self, place_name: str) -> int:
        number = self.db_provider.execute_read_query(
            '''SELECT COUNT(*) FROM matches WHERE start_time > NOW() AND place_name = %s;''',
            (place_name,)
        )[0][0]
        return number

    def read_by_group(self, group_id: int, limit: int, offset: int) -> list[Match]:
        rows = self.db_provider.execute_read_query(
            '''SELECT * from matches WHERE start_time > NOW() AND %s = ANY (group_id) ORDER BY start_time LIMIT %s OFFSET %s;''',
            (
                group_id,
                limit,
                offset,
            )
        )
        return list(map(match_from_row, rows))
    
    def count_by_group(self, group_id: int) -> int:
        number = self.db_provider.execute_read_query(
            '''SELECT COUNT(*) FROM matches WHERE start_time > NOW() AND %s = ANY (group_id);''',
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
    
    def read_notificapable(self) -> list[Match]:
        rows = self.db_provider.execute_read_query(
            '''SELECT * FROM matches WHERE start_time BETWEEN NOW() + INTERVAL 4 DAY AND NOW() + INTERVAL 5 DAY;''',
        )
        return list(map(match_from_row, rows))
    
    def set_on_match_created(self, callback: Callable[[Match], None]):
        self._on_match_created = callback
