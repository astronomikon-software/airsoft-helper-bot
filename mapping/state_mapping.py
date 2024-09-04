import json
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
        'progress': state.progress,
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
    }.get(
        dict_state['state_name'],
        MainMenuState
    )()


def dict_to_edit_match_state(dict_state: dict) -> EditMatchState:
    state = EditMatchState()
    state.match = Match()
    state.match.id = dict_state['match']['id']
    state.match.start_time = dict_state['match']['start_time']
    state.match.duration = dict_state['match']['duration']
    state.match.place_id = dict_state['match']['place_id']
    state.match.group_id = dict_state['match']['group_id']
    state.match.genre_id = dict_state['match']['genre_id']
    state.match.is_loneliness_friendly = dict_state['match']['is_loneliness_friendly']
    state.progress = dict_state['progress']
    return state
