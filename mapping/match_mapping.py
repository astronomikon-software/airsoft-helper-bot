from model.match import Match


def match_from_row(row: tuple) -> Match:
    match = Match()
    match.id = row[0]
    match.start_time = row[1]
    match.duration = row[2]
    match.place_id = row[3]
    match.group_id = row[4]
    match.genre_id = row[5]
    match.is_loneliness_friendly = row[6]
    return match
