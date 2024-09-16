from states_events.states import *


def progress_to_str(progress) -> str:
    return {
        EditMatchProgress.START_TIME: 'START_TIME',
        EditMatchProgress.START_TIME_AGAIN: 'START_TIME_AGAIN',
        EditMatchProgress.DURATION: 'DURATION',
        EditMatchProgress.PLACE: 'PLACE',
        EditMatchProgress.GROUP: 'GROUP',
        EditMatchProgress.GENRE: 'GENRE',
        EditMatchProgress.IS_LONELINESS_FRIENDLY: 'IS_LONELINESS_FRIENDLY',
        EditMatchProgress.CONFIRMATION:'CONFIRMATION',
        CalendarProgress.VEIW_ALL: 'VEIW_ALL',
        CalendarProgress.VEIW_ONE: 'VEIW_ONE',
        VeiwByPlaceProgress.VEIW_PLACES: 'VEIW_PLACES',
        VeiwByPlaceProgress.VEIW_FILTERED_BY_PLACE: 'VEIW_FILTERED_BY_PLACE',
        VeiwByPlaceProgress.VEIW_ONE_FILTERED_BY_PLACE: 'VEIW_ONE_FILTERED_BY_PLACE',
        VeiwByGroupProgress.VEIW_GROUPS: 'VEIW_GROUPS',
        VeiwByGroupProgress.VEIW_FILTERED_BY_GROUP: 'VEIW_FILTERED_BY_GROUP',
        VeiwByGroupProgress.VEIW_ONE_FILTERED_BY_GROUP: 'VEIW_ONE_FILTERED_BY_GROUP',
        VeiwByGenreProgress.VEIW_GENRES: 'VEIW_GENRES',
        VeiwByGenreProgress.VEIW_FILTERED_BY_GENRE: 'VEIW_FILTERED_BY_GENRE',
        VeiwByGenreProgress.VEIW_ONE_FILTERED_BY_GENRE: 'VEIW_ONE_FILTERED_BY_GENRE',
        VeiwByLonelinessProgress.CHOOSE_LONELINESS_STATUS: 'CHOOSE_LONELINESS_STATUS',
        VeiwByLonelinessProgress.VEIW_FILTERED_BY_LONELINESS: 'VEIW_FILTERED_BY_LONELINESS',
        VeiwByLonelinessProgress.VEIW_ONE_FILTERED_BY_LONELINESS: 'VEIW_ONE_FILTERED_BY_LONELINESS',
        UpdateMatchProgress.CHOOSE_GAME: 'CHOOSE_GAME',
        UpdateMatchProgress.CONFIRM_UPDATING: 'CONFIRM_UPDATING',
    }[progress]


def str_to_progress(str_progress: str):
    return {
        'START_TIME': EditMatchProgress.START_TIME,
        'START_TIME_AGAIN': EditMatchProgress.START_TIME_AGAIN,
        'DURATION': EditMatchProgress.DURATION,
        'PLACE': EditMatchProgress.PLACE,
        'GROUP': EditMatchProgress.GROUP,
        'GENRE': EditMatchProgress. GENRE,
        'IS_LONELINESS_FRIENDLY': EditMatchProgress.IS_LONELINESS_FRIENDLY,
        'CONFIRMATION': EditMatchProgress.CONFIRMATION,
        'VEIW_ALL': CalendarProgress.VEIW_ALL,
        'VEIW_ONE': CalendarProgress.VEIW_ONE,
        'VEIW_PLACES': VeiwByPlaceProgress.VEIW_PLACES,
        'VEIW_FILTERED_BY_PLACE': VeiwByPlaceProgress.VEIW_FILTERED_BY_PLACE,
        'VEIW_ONE_FILTERED_BY_PLACE': VeiwByPlaceProgress.VEIW_ONE_FILTERED_BY_PLACE,
        'VEIW_GROUPS': VeiwByGroupProgress.VEIW_GROUPS,
        'VEIW_FILTERED_BY_GROUP': VeiwByGroupProgress.VEIW_FILTERED_BY_GROUP,
        'VEIW_ONE_FILTERED_BY_GROUP': VeiwByGroupProgress.VEIW_ONE_FILTERED_BY_GROUP,
        'VEIW_GENRES': VeiwByGenreProgress.VEIW_GENRES,
        'VEIW_FILTERED_BY_GENRE': VeiwByGenreProgress.VEIW_FILTERED_BY_GENRE,
        'VEIW_ONE_FILTERED_BY_GENRE': VeiwByGenreProgress.VEIW_ONE_FILTERED_BY_GENRE,
        'CHOOSE_LONELINESS_STATUS': VeiwByLonelinessProgress.CHOOSE_LONELINESS_STATUS,
        'VEIW_FILTERED_BY_LONELINESS': VeiwByLonelinessProgress.VEIW_FILTERED_BY_LONELINESS,
        'VEIW_ONE_FILTERED_BY_LONELINESS': VeiwByLonelinessProgress.VEIW_ONE_FILTERED_BY_LONELINESS,
        'CHOOSE_GAME': UpdateMatchProgress.CHOOSE_GAME,
        'CONFIRM_UPDATING': UpdateMatchProgress.CONFIRM_UPDATING,
    }[str_progress]
