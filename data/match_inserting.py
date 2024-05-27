from execution import execute_query
from model.match import Match


def insert_match(connection, match: Match):
    
    match = Match()
    match_id = match.id
    start_time = match.start_time
    duration = match.duration
    place_id = match.place_id
    group_id = match.group_id
    genre_id = match.genre_id
    is_loneliness_friendly = match.is_loneliness_friendly
    match_records = (start_time, duration, place_id, group_id, genre_id, is_loneliness_friendly)

    insert_query = (
    f"INSERT INTO matches (start_time, duration, place_id, group_id, genre_id, is_loneliness_friendly) VALUES {match_records}"
    )

    execute_query(connection, insert_query)
