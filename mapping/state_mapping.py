import json
from mapping.progress_mapping import progress_to_str, str_to_progress
from states_events.states import *


def state_to_dict(state: BotState) -> dict:
    if isinstance(state, EditMatchState):
        return edit_match_state_to_dict(state)
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
            'duration': state.match.duration,
            'place_id': state.match.place_id,
            'group_id': state.match.group_id,
            'genre_id': state.match.genre_id,
            'is_loneliness_friendly': state.match.is_loneliness_friendly
        },
        'progress': progress_to_str(state.progress),
    }


def dict_to_state(dict_state: dict) -> BotState:
    if dict_state['state_name'] == 'EditMatchState':
        return dict_to_edit_match_state(dict_state)
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
    match.duration = dict_state['match']['duration']
    match.place_id = dict_state['match']['place_id']
    match.group_id = dict_state['match']['group_id']
    match.genre_id = dict_state['match']['genre_id']
    match.is_loneliness_friendly = dict_state['match']['is_loneliness_friendly']    
    state = EditMatchState(
        match=match,
        progress=str_to_progress(dict_state['progress']),
    )
    return state
