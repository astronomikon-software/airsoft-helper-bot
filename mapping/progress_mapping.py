from states_events.states import EditMatchState, CalendarState


def progress_to_str(progress: EditMatchState.Progress) -> str:
    return {
        EditMatchState.Progress.START_TIME: 'START_TIME',
        EditMatchState.Progress.START_TIME_AGAIN: 'START_TIME_AGAIN',
        EditMatchState.Progress.DURATION: 'DURATION',
        EditMatchState.Progress.PLACE: 'PLACE',
        EditMatchState.Progress.GROUP: 'GROUP',
        EditMatchState.Progress.GENRE: 'GENRE',
        EditMatchState.Progress.IS_LONELINESS_FRIENDLY: 'IS_LONELINESS_FRIENDLY',
        EditMatchState.Progress.CONFIRMATION:'CONFIRMATION',
        CalendarState.Progress.VEIW_ALL: 'VEIW_ALL',
        CalendarState.Progress.VEIW_ONE: 'VEIW_ONE',
    }[progress]


def str_to_progress(str_progress: str) -> EditMatchState.Progress:
    return {
        'START_TIME': EditMatchState.Progress.START_TIME,
        'START_TIME_AGAIN': EditMatchState.Progress.START_TIME_AGAIN,
        'DURATION': EditMatchState.Progress.DURATION,
        'PLACE': EditMatchState.Progress.PLACE,
        'GROUP': EditMatchState.Progress.GROUP,
        'GENRE': EditMatchState.Progress. GENRE,
        'IS_LONELINESS_FRIENDLY': EditMatchState.Progress.IS_LONELINESS_FRIENDLY,
        'CONFIRMATION': EditMatchState.Progress.CONFIRMATION,
        'VEIW_ALL': CalendarState.Progress.VEIW_ALL,
        'VEIW_ONE': CalendarState.Progress.VEIW_ONE,
    }[str_progress]
