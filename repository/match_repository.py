from model.match import Match
from model.genre import Genre
from model.group import Group
from model.place import Place

from data.execution import execute_query
from data.read_all_execution import execute_read_query

from mapping.match_mapping import match_from_row


class MatchRepository:

    def create(self, connection, match: Match):
        insert_match = f'''
        INSERT INTO matches (
            start_time, 
            duration, 
            place_id, 
            group_id, 
            genre_id, 
            is_loneliness_friendly
            ) 
        VALUES (
            {match.start_time},
            {match.duration},
            {match.place_id}, 
            {match.group_id}, 
            {match.genre_id}, 
            {match.is_loneliness_friendly}
            )
            '''

        execute_query(connection, insert_match)
    
    def update(self, connection, match: Match):
        update_match = f'''
            UPDATE
                matches
            SET
                start_time = {match.start_time},
                start_date = {match.start_date},
                duration = {match.duration},
                place_id = {match.place_id},
                group_id = {match.group_id},
                genre_id = {match.genre_id},
                is_loneliness_friendly = {match.is_loneliness_friendly}
            WHERE
                id = {match.id}
            '''
        
        execute_query(connection, update_match)

    def delete(self, connection, match: Match):
        delete_match = f'DELETE FROM matches WHERE id = {match.id}'
        execute_query(connection, delete_match)

    def read_all(self, connection) -> list[Match]:
        list_of_matches = []
        select_all_matches = 'SELECT * from matches'
        matches = execute_read_query(connection, select_all_matches)

        for row in matches:
            match = match_from_row(row)
            list_of_matches.append(match)
        
        return list_of_matches

    def filter_by_genre(self, connection, genre: Genre) -> list[Match]:
        list_of_matches = []
        select_matches = f'SELECT * from matches WHERE genre_id = {genre.id}'
        matches = execute_read_query(connection, select_matches)

        for match in matches:
            list_of_matches.append(match)
        
        return list_of_matches

    def filter_by_place(self, connection, place: Place) -> list[Match]:
        list_of_matches = []
        select_matches = f'SELECT * from matches WHERE place_id = {place.id}'
        matches = execute_read_query(connection, select_matches)

        for row in matches:
            match = match_from_row(row)
            list_of_matches.append(match)
        
        return list_of_matches

    def filter_by_group(self, connection, group: Group) -> list[Match]:
        list_of_matches = []
        select_matches = f'SELECT * from matches WHERE group_id = {group.id}'
        matches = execute_read_query(connection, select_matches)

        for row in matches:
            match = match_from_row(row)
            list_of_matches.append(match)
        
        return list_of_matches

    def filter_by_solo_friendliness(self, connection) -> list[Match]:
        list_of_matches = []
        select_matches = 'SELECT * from matches WHERE is_loneliness_friendly is true'
        matches = execute_read_query(connection, select_matches)

        for row in matches:
            match = match_from_row(row)
            list_of_matches.append(match)
        
        return list_of_matches
