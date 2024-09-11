from states_events.states import *


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
        VeiwByPlaceState.Progress.VEIW_PLACES: 'VEIW_PLACES',
        VeiwByPlaceState.Progress.VEIW_FILTERED_BY_PLACE: 'VEIW_FILTERED_BY_PLACE',
        VeiwByPlaceState.Progress.VEIW_ONE_FILTERED_BY_PLACE: 'VEIW_ONE_FILTERED_BY_PLACE',
        VeiwByGroupState.Progress.VEIW_GROUPS: 'VEIW_GROUPS',
        VeiwByGroupState.Progress.VEIW_FILTERED_BY_GROUP: 'VEIW_FILTERED_BY_GROUP',
        VeiwByGroupState.Progress.VEIW_ONE_FILTERED_BY_GROUP: 'VEIW_ONE_FILTERED_BY_GROUP',
        VeiwByGenreState.Progress.VEIW_GENRES: 'VEIW_GENRES',
        VeiwByGenreState.Progress.VEIW_FILTERED_BY_GENRE: 'VEIW_FILTERED_BY_GENRE',
        VeiwByGenreState.Progress.VEIW_ONE_FILTERED_BY_GENRE: 'VEIW_ONE_FILTERED_BY_GENRE',
        VeiwByLonelinessState.Progress.CHOOSE_LONELINESS_STATUS: 'CHOOSE_LONELINESS_STATUS',
        VeiwByLonelinessState.Progress.VEIW_FILTERED_BY_LONELINESS: 'VEIW_FILTERED_BY_LONELINESS',
        VeiwByLonelinessState.Progress.VEIW_ONE_FILTERED_BY_LONELINESS: 'VEIW_ONE_FILTERED_BY_LONELINESS',
        UpdateMatchState.Progress.CHOOSE_GAME: 'CHOOSE_GAME',
        UpdateMatchState.Progress.CONFIRM_UPDATING: 'CONFIRM_UPDATING',
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
        'VEIW_PLACES': VeiwByPlaceState.Progress.VEIW_PLACES,
        'VEIW_FILTERED_BY_PLACE': VeiwByPlaceState.Progress.VEIW_FILTERED_BY_PLACE,
        'VEIW_ONE_FILTERED_BY_PLACE': VeiwByPlaceState.Progress.VEIW_ONE_FILTERED_BY_PLACE,
        'VEIW_GROUPS': VeiwByGroupState.Progress.VEIW_GROUPS,
        'VEIW_FILTERED_BY_GROUP': VeiwByGroupState.Progress.VEIW_FILTERED_BY_GROUP,
        'VEIW_ONE_FILTERED_BY_GROUP': VeiwByGroupState.Progress.VEIW_ONE_FILTERED_BY_GROUP,
        'VEIW_GENRES': VeiwByGenreState.Progress.VEIW_GENRES,
        'VEIW_FILTERED_BY_GENRE': VeiwByGenreState.Progress.VEIW_FILTERED_BY_GENRE,
        'VEIW_ONE_FILTERED_BY_GENRE': VeiwByGenreState.Progress.VEIW_ONE_FILTERED_BY_GENRE,
        'CHOOSE_LONELINESS_STATUS': VeiwByLonelinessState.Progress.CHOOSE_LONELINESS_STATUS,
        'VEIW_FILTERED_BY_LONELINESS': VeiwByLonelinessState.Progress.VEIW_FILTERED_BY_LONELINESS,
        'VEIW_ONE_FILTERED_BY_LONELINESS': VeiwByLonelinessState.Progress.VEIW_ONE_FILTERED_BY_LONELINESS,
        'CHOOSE_GAME': UpdateMatchState.Progress.CHOOSE_GAME,
        'CONFIRM_UPDATING': UpdateMatchState.Progress.CONFIRM_UPDATING,
    }[str_progress]
