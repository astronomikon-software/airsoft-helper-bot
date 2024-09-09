from states_events.states import *


def progress_to_str(progress: SetNewMatchState.Progress) -> str:
    return {
        SetNewMatchState.Progress.START_TIME: 'START_TIME',
        SetNewMatchState.Progress.START_TIME_AGAIN: 'START_TIME_AGAIN',
        SetNewMatchState.Progress.DURATION: 'DURATION',
        SetNewMatchState.Progress.PLACE: 'PLACE',
        SetNewMatchState.Progress.GROUP: 'GROUP',
        SetNewMatchState.Progress.GENRE: 'GENRE',
        SetNewMatchState.Progress.IS_LONELINESS_FRIENDLY: 'IS_LONELINESS_FRIENDLY',
        SetNewMatchState.Progress.CONFIRMATION:'CONFIRMATION',
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
    }[progress]


def str_to_progress(str_progress: str) -> SetNewMatchState.Progress:
    return {
        'START_TIME': SetNewMatchState.Progress.START_TIME,
        'START_TIME_AGAIN': SetNewMatchState.Progress.START_TIME_AGAIN,
        'DURATION': SetNewMatchState.Progress.DURATION,
        'PLACE': SetNewMatchState.Progress.PLACE,
        'GROUP': SetNewMatchState.Progress.GROUP,
        'GENRE': SetNewMatchState.Progress. GENRE,
        'IS_LONELINESS_FRIENDLY': SetNewMatchState.Progress.IS_LONELINESS_FRIENDLY,
        'CONFIRMATION': SetNewMatchState.Progress.CONFIRMATION,
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
    }[str_progress]
