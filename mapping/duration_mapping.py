from model.duration import Duration


def duration_from_row(row: tuple) -> Duration:
    duration = Duration()
    duration.id = row[0]
    duration.name = row[1]
    return duration
