from model.match import Match

def match_from_row(row: tuple) -> Match:
    match = Match()
    match.id = row[0]
    match.start_date = row[1]
    match.start_time = row[2]
    match.duration = row[3]
    match.place_id = row[4]
    match.group_id = row[5]
    match.genre_id = row[6]
    match.is_loneliness_friendly = row[7]
    return match
