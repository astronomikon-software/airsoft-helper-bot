from model.match import Match
from mapping.datetime_mapping import datetime_to_int, int_to_datetime


def match_from_row(row: tuple) -> Match:
    return Match(
        id = row[0],
        name = row[1],
        start_time = datetime_to_int(row[2]),
        duration_id=row[3],
        place_name = row[4],
        group_id = row[5],
        genre_id = row[6],
        is_loneliness_friendly = row[7],
        url = row[8],
        annotation=row[9]
    )

def row_from_match(match: Match) -> tuple:
    int_start_time = int_to_datetime(match.start_time)
    row = (
        match.name,
        int_start_time,
        match.duration_id,
        match.place_name,
        match.group_id,
        match.genre_id,
        match.is_loneliness_friendly,
        match.url,
        match.annotation,
    )
    return row
