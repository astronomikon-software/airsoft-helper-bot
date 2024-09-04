from model.user import User
from states_events.menu_content.button_callbacks import ButtonCallback
from states_events.states import *
from states_events.events import *


def get_new_state(state: BotState, event: BotEvent, user: User) -> BotState:
    if isinstance(event, ButtonEvent):
        state = {
            ButtonCallback.MAIN_MENU: MainMenuState,
            ButtonCallback.HOW_TO: HowToState,
            ButtonCallback.MARKET: MarketState,
            ButtonCallback.SCHEDULE: ScheduleState,
            ButtonCallback.CALENDAR: CalendarState,
            ButtonCallback.ORGANISERS: OrganisersState,
            ButtonCallback.FILTERS: FiltersState,
            ButtonCallback.SET_DATETIME: EditMatchState,
        }[event.callback]()
        if state is not None:
            return state
    
    if isinstance(event, MessageEvent):
        if event.text == '/start':
            return MainMenuState()
        # elif event.text == some regexp 

    if isinstance(state, EditMatchState):
        return on_edit_match_state(state)
    
        
def on_edit_match_state(state: EditMatchState, event: BotEvent):
    match = state.match
    if (state.progress == EditMatchState.Progress.DURATION) \
        and isinstance(event, MessageEvent):
        match.duration = duration_from_str(event.text)
        return EditMatchState(
            match=match,
            progress=EditMatchState.Progress.GENRE,
        ) 
    elif (state.progress == EditMatchState.Progress.PLACE) \
        and isinstance(event, ButtonEvent):
        match.place_id = match_id_from_callback(event.callback)
        return EditMatchState(
            match=match,
            progress=EditMatchState.Progress.GENRE,
        )
    elif (state.progress == EditMatchState.Progress.CONFIRMATION) \
        and isinstance(event, ButtonEvent):
        is_confirmed = is_confirmed_from_callback(event.callback)
        if is_confirmed:
            # match_repository.create() # TODO
            return MainMenuState()
