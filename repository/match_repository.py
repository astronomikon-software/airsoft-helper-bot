from model.match import Match
from model.genre import Genre
from model.group import Group
from model.place import Place

from data.connection import connection
from data.execution import execute_query
from data.read_all_execution import execute_read_query

from mapping.match_mapping import match_from_row

from utils.datetime_util import int_to_datetime


class MatchRepository:

    def create(self, match: Match):
        start_time_obj = int_to_datetime(match.start_time)
        duration_obj = int_to_datetime(match.duration)
        insert_formula = '''INSERT INTO matches (start_time, duration, place_id, group_id, genre_id, is_loneliness_friendly) VALUES (%s, %s, %s, %s, %s, %s)'''
        insert_values = (start_time_obj, duration_obj, match.place_id, match.group_id, match.genre_id, match.is_loneliness_friendly)
        execute_query(connection, insert_formula, insert_values)
    
    def update(self, match: Match):
        start_time_obj = int_to_datetime(match.start_time)
        duration_obj = int_to_datetime(match.duration)
        update_formula = '''UPDATE matches SET start_time = %s, duration = %s, place_id = %s, group_id = %s, genre_id = %s, is_loneliness_friendly = %s WHERE id = %s'''
        update_values = (start_time_obj, duration_obj, match.place_id, match.group_id, match.genre_id, match.is_loneliness_friendly, match.id)
        execute_query(connection, update_formula, update_values)

    def delete(self, match: Match):
        delete_formula = '''DELETE FROM matches WHERE id = %s'''
        delete_values = (match.id,)
        execute_query(connection, delete_formula, delete_values)

    def read_all(self) -> list[Match]:
        select_formula = '''SELECT * from matches'''
        select_values = set()
        matches = execute_read_query(connection, select_formula, select_values)
        list_of_matches = list(map(match_from_row, matches))
        return list_of_matches

    def read_by_genre(self, genre: Genre) -> list[Match]:
        select_formula = '''SELECT * from matches WHERE genre_id = %s'''
        select_values = (genre.id,)
        matches = execute_read_query(connection, select_formula, select_values)
        list_of_matches = list(map(match_from_row, matches))
        return list_of_matches

    def read_by_place(self, place: Place) -> list[Match]:
        select_formula = '''SELECT * from matches WHERE place_id = %s'''
        select_values = (place.id,)
        matches = execute_read_query(connection, select_formula, select_values)
        list_of_matches = list(map(match_from_row, matches))
        return list_of_matches

    def read_by_group(self, group: Group) -> list[Match]:
        select_formula = '''SELECT * from matches WHERE group_id = %s'''
        select_values = (group.id,)
        matches = execute_read_query(connection, select_formula, select_values)
        list_of_matches = list(map(match_from_row, matches))
        return list_of_matches

    def read_by_solo_friendliness(self) -> list[Match]:
        select_formula = '''SELECT * from matches WHERE is_loneliness_friendly is %s'''
        select_values = (True,)
        matches = execute_read_query(connection, select_formula, select_values)
        list_of_matches = list(map(match_from_row, matches))
        return list_of_matches
