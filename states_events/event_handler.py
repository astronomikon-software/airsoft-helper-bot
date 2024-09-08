from model.user import User
from repository.repository_initiation import match_repository
from states_events.menu_content.button_callbacks import ButtonCallback
from states_events.states import *
from states_events.events import *
from utils.datetime_util import check_datetime_format
from mapping.datetime_mapping import str_time_to_int
from mapping.loneliness_mapping import str_to_loneliness
from mapping.confirmation_mapping import str_to_confirmation


def get_new_state(state: BotState, event: BotEvent, user: User) -> BotState:
    if isinstance(event, ButtonEvent) and event.callback == ButtonCallback.MAIN_MENU:
        return MainMenuState()
    
    if isinstance(event, MessageEvent) and event.text == '/start':
        return MainMenuState()
    
    if isinstance(state, EditMatchState) and user.is_admin:
        return on_edit_match_state(state, event, user)
    
    if isinstance(state, CalendarState) and isinstance(event, ButtonEvent) and state.progress == CalendarState.Progress.VEIW_ALL:
        return on_calendar_state(state, event)
    
    if isinstance(event, ButtonEvent):
        state_class = {
            ButtonCallback.MAIN_MENU: MainMenuState,
            ButtonCallback.HOW_TO: HowToState,
            ButtonCallback.MARKET: MarketState,
            ButtonCallback.SCHEDULE: ScheduleState,
            ButtonCallback.CALENDAR: CalendarState,
            ButtonCallback.ORGANISERS: OrganisersState,
            ButtonCallback.FILTERS: FiltersState,
            ButtonCallback.SET_DATETIME: EditMatchState,
            ButtonCallback.CALENDAR: CalendarState,
        }[event.callback]
        if state_class is not None:
            if state_class is EditMatchState:
                match = Match()
                match.id = 0
                match.start_time = 0
                match.start_time = 0
                match.duration = 0
                match.place_id = 0
                match.group_id = 0
                match.genre_id = 0
                match.is_loneliness_friendly = False
                return state_class(match=match, progress=EditMatchState.Progress.START_TIME)
            elif state_class is CalendarState:
                return state_class(0, CalendarState.Progress.VEIW_ALL)
            else:
                return state_class()
    
    if isinstance(event, MessageEvent):
        if event.text == '/start':
            return MainMenuState()
        # elif event.text == some regexp 
    
        
def on_edit_match_state(state: EditMatchState, event: BotEvent, user: User):
    match = state.match
    if (state.progress == EditMatchState.Progress.START_TIME) \
        and isinstance(event, MessageEvent):
        try:
            match.start_time = str_time_to_int(event.text)
            return EditMatchState(
                match=match,
                progress=EditMatchState.Progress.PLACE,
            )
        except:
            return EditMatchState(
                match=match,
                progress=EditMatchState.Progress.START_TIME_AGAIN,
            )
    elif (state.progress == EditMatchState.Progress.START_TIME_AGAIN) \
        and isinstance(event, MessageEvent):
        try:
            match.start_time = str_time_to_int(event.text)
            return EditMatchState(
                match=match,
                progress=EditMatchState.Progress.PLACE,
            )
        except:
            return EditMatchState(
                match=match,
                progress=EditMatchState.Progress.START_TIME_AGAIN,
            )
    elif (state.progress == EditMatchState.Progress.PLACE) \
        and isinstance(event, ButtonEvent):
        match.place_id = int(event.callback)
        return EditMatchState(
            match=match,
            progress=EditMatchState.Progress.GROUP,
        )
    elif (state.progress == EditMatchState.Progress.GROUP) \
        and isinstance(event, ButtonEvent):
        match.group_id = int(event.callback)
        return EditMatchState(
            match=match,
            progress=EditMatchState.Progress.GENRE,
        )
    elif (state.progress == EditMatchState.Progress.GENRE) \
        and isinstance(event, ButtonEvent):
        match.genre_id = int(event.callback)
        return EditMatchState(
            match=match,
            progress=EditMatchState.Progress.IS_LONELINESS_FRIENDLY,
        )
    elif (state.progress == EditMatchState.Progress.IS_LONELINESS_FRIENDLY) \
        and isinstance(event, ButtonEvent):
        match.is_loneliness_friendly = str_to_loneliness(event.callback)
        return EditMatchState(
            match=match,
            progress=EditMatchState.Progress.CONFIRMATION,
        )
    elif (state.progress == EditMatchState.Progress.CONFIRMATION) \
        and isinstance(event, ButtonEvent):
        is_confirmed = str_to_confirmation(event.callback)
        if is_confirmed:
            match_repository.create(match=match)
            return GameIsSavedState()
        else:
            return GameIsCancelledState()


def on_calendar_state(state: CalendarState, event: ButtonEvent):
    if event.callback == ButtonCallback.SCHEDULE:
        return ScheduleState()
    if state.progress == CalendarState.Progress.VEIW_ALL:
        return CalendarState(
            match_id=int(event.callback), 
            progress=CalendarState.Progress.VEIW_ONE
        )
