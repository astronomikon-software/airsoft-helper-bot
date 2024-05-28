from model.match import Match
from model.genre import Genre
from model.group import Group
from model.place import Place

from data.execution import execute_query
from data.connection import create_connection


class MatchRepository:

    def create(self, match: Match):
        
        match = Match()
        match_records = (
            match.start_time, 
            match.duration, 
            match.place_id, 
            match.group_id, 
            match.genre_id, 
            match.is_loneliness_friendly
            )

        insert_query = (
        f'INSERT INTO matches (start_time, duration, place_id, group_id, genre_id, is_loneliness_friendly) VALUES {match_records}'
        )

        connection = create_connection()
        execute_query(connection, insert_query)
    
    def update(self, match: Match):
        
        match = Match()
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
         
        connection = create_connection()
        execute_query(connection, update_match)

    def delete(self, match: Match):

        match = Match()
        delete_match = f'DELETE FROM matches WHERE id = {match.id}'

        connection = create_connection()
        execute_query(connection, delete_match)

    async def read_all(self, match: Match) -> list[Match]:
        pass

    async def filter_by_genre(self, genre: Genre) -> list[Match]:
        pass

    async def filter_by_place(self, place: Place) -> list[Match]:
        pass

    async def filter_by_group(self, group: Group) -> list[Match]:
        pass

    async def filter_by_solo_friendliness(self) -> list[Match]:
        pass

