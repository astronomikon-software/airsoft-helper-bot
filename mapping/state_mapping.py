import json
from mapping.progress_mapping import progress_to_str, str_to_progress
from states_events.states import *


def state_to_dict(state: BotState) -> dict:
    if isinstance(state, EditMatchState):
        return edit_match_state_to_dict(state)
    elif isinstance(state, CalendarState):
        return calendar_state_to_dict(state)
    elif isinstance(state, VeiwByPlaceState):
        return veiw_by_place_state_to_dict(state)
    elif isinstance(state, VeiwByGroupState):
        return veiw_by_group_state_to_dict(state)
    elif isinstance(state, VeiwByGenreState):
        return veiw_by_genre_state_to_dict(state)
    elif isinstance(state, VeiwByLonelinessState):
        return veiw_by_loneliness_state_to_dict(state)
    elif isinstance(state, UpdateMatchState):
        return update_match_state_to_dict(state)
    else:
        return simple_state_to_dict(state)


def simple_state_to_dict(state: BotState) -> dict:
    return {
        'state_name': state.__class__.__name__,
    }


def edit_match_state_to_dict(state: EditMatchState) -> dict:
    return {
        'state_name': 'EditMatchState',
        'match': {
            'id': state.match.id,
            'start_time': state.match.start_time,
            'place_id': state.match.place_id,
            'group_id': state.match.group_id,
            'genre_id': state.match.genre_id,
            'is_loneliness_friendly': state.match.is_loneliness_friendly
        },
        'progress': progress_to_str(state.progress),
    }


def calendar_state_to_dict(state: CalendarState) -> dict:
    return {
        'state_name': 'CalendarState',
        'match_id': state.match_id,
        'page_number': state.page_number,
        'progress': progress_to_str(state.progress)
    }


def veiw_by_place_state_to_dict(state: VeiwByPlaceState) -> dict:
    return {
        'state_name': 'VeiwByPlaceState',
        'item_id': state.item_id,
        'match_id': state.match_id,
        'page_number': state.page_number,
        'progress': progress_to_str(state.progress)
    }

def veiw_by_group_state_to_dict(state: VeiwByGroupState) -> dict:
    return {
        'state_name': 'VeiwByGroupState',
        'item_id': state.item_id,
        'match_id': state.match_id,
        'page_number': state.page_number,
        'progress': progress_to_str(state.progress)
    }

def veiw_by_genre_state_to_dict(state: VeiwByGenreState) -> dict:
    return {
        'state_name': 'VeiwByGenreState',
        'item_id': state.item_id,
        'match_id': state.match_id,
        'page_number': state.page_number,
        'progress': progress_to_str(state.progress)
    }

def veiw_by_loneliness_state_to_dict(state: VeiwByLonelinessState) -> dict:
    return {
        'state_name': 'VeiwByLonelinessState',
        'status': state.status,
        'match_id': state.match_id,
        'page_number': state.page_number,
        'progress': progress_to_str(state.progress)
    }

def update_match_state_to_dict(state: UpdateMatchState) -> dict:
    return {
        'state_name': 'UpdateMatchState',
        'match_id': state.match_id,
        'page_number': state.page_number,
        'progress': progress_to_str(state.progress)
    }

# reverse

def dict_to_state(dict_state: dict) -> BotState:
    if dict_state['state_name'] == 'EditMatchState':
        return dict_to_edit_match_state(dict_state)
    elif dict_state['state_name'] == 'CalendarState':
        return dict_to_calendar_state(dict_state)
    elif dict_state['state_name'] == 'VeiwByPlaceState':
        return dict_to_veiw_by_place_state(dict_state)
    elif dict_state['state_name'] == 'VeiwByGroupState':
        return dict_to_veiw_by_group_state(dict_state)
    elif dict_state['state_name'] == 'VeiwByGenreState':
        return dict_to_veiw_by_genre_state(dict_state)
    elif dict_state['state_name'] == 'VeiwByLonelinessState':
        return dict_to_veiw_by_loneliness_state(dict_state)
    elif dict_state['state_name'] == 'UpdateMatchState':
        return dict_to_update_match_state(dict_state)
    else:
        return dict_to_simple_state(dict_state)


def dict_to_simple_state(dict_state: dict) -> BotState:
    return {
        'MainMenuState': MainMenuState,
        'StartState': StartState,
        'MarketState': MarketState,
        'HowToState': HowToState,
        'CalendarState': CalendarState,
        'FiltersState': FiltersState,
        'OrganisersState': OrganisersState,
        'GameIsSavedState': GameIsSavedState,
        'GameIsCancelledState': GameIsCancelledState
    }.get(
        dict_state['state_name'],
        MainMenuState
    )()


def dict_to_edit_match_state(dict_state: dict) -> EditMatchState:
    match = Match()
    match.id = dict_state['match']['id']
    match.start_time = dict_state['match']['start_time']
    match.place_id = dict_state['match']['place_id']
    match.group_id = dict_state['match']['group_id']
    match.genre_id = dict_state['match']['genre_id']
    match.is_loneliness_friendly = dict_state['match']['is_loneliness_friendly']    
    state = EditMatchState(
        match=match,
        progress=str_to_progress(dict_state['progress']),
    )
    return state


def dict_to_calendar_state(dict_state: dict) -> CalendarState:
    return CalendarState(
        match_id=dict_state['match_id'],
        page_number=dict_state['page_number'],
        progress=str_to_progress(dict_state['progress'])
    ) 

def dict_to_veiw_by_place_state(dict_state: dict) -> VeiwByPlaceState:
    return VeiwByPlaceState(
        item_id=dict_state['item_id'],
        match_id=dict_state['match_id'],
        page_number=dict_state['page_number'],
        progress=str_to_progress(dict_state['progress'])
    )

def dict_to_veiw_by_group_state(dict_state: dict) -> VeiwByGroupState:
    return VeiwByGroupState(
        item_id=dict_state['item_id'],
        match_id=dict_state['match_id'],
        page_number=dict_state['page_number'],
        progress=str_to_progress(dict_state['progress'])
    )

def dict_to_veiw_by_genre_state(dict_state: dict) -> VeiwByGenreState:
    return VeiwByGenreState(
        item_id=dict_state['item_id'],
        match_id=dict_state['match_id'],
        page_number=dict_state['page_number'],
        progress=str_to_progress(dict_state['progress'])
    )

def dict_to_veiw_by_loneliness_state(dict_state: dict) -> VeiwByLonelinessState:
    return VeiwByLonelinessState(
        status=dict_state['status'],
        match_id=dict_state['match_id'],
        page_number=dict_state['page_number'],
        progress=str_to_progress(dict_state['progress'])
    )

def dict_to_update_match_state(dict_state: dict) -> UpdateMatchState:
    return UpdateMatchState(
        match_id=dict_state['match_id'],
        page_number=dict_state['page_number'],
        progress=str_to_progress(dict_state['progress'])
    )
