from states_events.states import EditMatchState


def progress_to_str(progress: EditMatchState.Progress) -> str:
    return {
        EditMatchState.Progress.START_TIME: 'START_TIME',
        EditMatchState.Progress.DURATION: 'DURATION',
        EditMatchState.Progress.PLACE: 'PLACE',
        EditMatchState.Progress.GROUP: 'GROUP',
        EditMatchState.Progress.GENRE: 'GENRE',
        EditMatchState.Progress.IS_LONELINESS_FRIENDLY: 'IS_LONELINESS_FRIENDLY',
        EditMatchState.Progress.CONFIRMATION:'CONFIRMATION',
    }[progress]


def str_to_progress(str_progress: str) -> EditMatchState.Progress:
    return {
        'START_TIME': EditMatchState.Progress.START_TIME,
        'DURATION': EditMatchState.Progress.DURATION,
        'PLACE': EditMatchState.Progress.PLACE,
        'GROUP': EditMatchState.Progress.GROUP,
        'GENRE': EditMatchState.Progress. GENRE,
        'IS_LONELINESS_FRIENDLY': EditMatchState.Progress.IS_LONELINESS_FRIENDLY,
        'CONFIRMATION': EditMatchState.Progress.CONFIRMATION,
    }[str_progress]
