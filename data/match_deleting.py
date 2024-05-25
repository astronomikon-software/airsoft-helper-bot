from execution import execute_query
from model.match import Match


def delete_match(connection, match: Match):
    
    match = Match()
    match_id = match.id
    
    delete_match = f"DELETE FROM matches WHERE id = {match_id}"
    execute_query(connection, delete_match)
