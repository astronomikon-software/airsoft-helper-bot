from model.match import Match
from mapping.datetime_mapping import datetime_to_int, int_to_datetime


def match_from_row(row: tuple) -> Match:
    return Match(
        id = row[0],
        start_time = datetime_to_int(row[1]),
        place_id = row[2],
        group_id = row[3],
        genre_id = row[4],
        is_loneliness_friendly = row[5],
    )

def row_from_match(match: Match) -> tuple:
    int_start_time = int_to_datetime(match.start_time)
    row = (
        int_start_time,
        match.place_id,
        match.group_id,
        match.genre_id,
        match.is_loneliness_friendly
    )
    return row
