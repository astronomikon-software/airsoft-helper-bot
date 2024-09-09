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

    if isinstance(state, SetNewMatchState) and user.is_admin:
        return on_edit_match_state(state, event, user)

    if isinstance(state, CalendarState) and isinstance(event, ButtonEvent) and state.progress == CalendarState.Progress.VEIW_ALL:
        return on_calendar_state(state, event)

    if isinstance(state, VeiwByPlaceState):
        return on_veiw_by_place_state(state, event)

    if isinstance(state, VeiwByGroupState):
        return on_veiw_by_group_state(state, event)

    if isinstance(state, VeiwByGenreState):
        return on_veiw_by_genre_state(state, event)
    
    if isinstance(state, VeiwByLonelinessState):
        return on_veiw_by_loneliness_state(state, event)

    if isinstance(event, ButtonEvent):
        state_class = {
            ButtonCallback.MAIN_MENU: MainMenuState,
            ButtonCallback.HOW_TO: HowToState,
            ButtonCallback.MARKET: MarketState,
            ButtonCallback.SCHEDULE: ScheduleState,
            ButtonCallback.CALENDAR: CalendarState,
            ButtonCallback.FILTERS: FiltersState,
            ButtonCallback.CHOOSE_PLACE: VeiwByPlaceState,
            ButtonCallback.CHOOSE_GROUP: VeiwByGroupState,
            ButtonCallback.CHOOSE_GENRE: VeiwByGenreState,
            ButtonCallback.LONELINESS: VeiwByLonelinessState,
            ButtonCallback.ORGANISERS: OrganisersState,
            ButtonCallback.SET_DATETIME: SetNewMatchState,
            ButtonCallback.CALENDAR: CalendarState,
        }[event.callback]
        if state_class is not None:
            if state_class is SetNewMatchState:
                match = Match()
                match.id = 0
                match.start_time = 0
                match.start_time = 0
                match.duration = 0
                match.place_id = 0
                match.group_id = 0
                match.genre_id = 0
                match.is_loneliness_friendly = False
                return state_class(match=match, progress=SetNewMatchState.Progress.START_TIME)
            elif state_class is CalendarState:
                return state_class(0, CalendarState.Progress.VEIW_ALL)
            elif state_class is VeiwByPlaceState:
                return state_class(0, 0, VeiwByPlaceState.Progress.VEIW_PLACES)
            elif state_class is VeiwByGroupState:
                return state_class(0, 0, VeiwByGroupState.Progress.VEIW_GROUPS)
            elif state_class is VeiwByGenreState:
                return state_class(0, 0, VeiwByGenreState.Progress.VEIW_GENRES)
            elif state_class is VeiwByLonelinessState:
                return state_class(ButtonCallback.FALSE, 0, VeiwByLonelinessState.Progress.CHOOSE_LONELINESS_STATUS)
            else:
                return state_class()
    
    if isinstance(event, MessageEvent):
        if event.text == '/start':
            return MainMenuState()
        # elif event.text == some regexp 
    
        
def on_edit_match_state(state: SetNewMatchState, event: BotEvent, user: User):
    match = state.match
    if (state.progress == SetNewMatchState.Progress.START_TIME) \
        and isinstance(event, MessageEvent):
        try:
            match.start_time = str_time_to_int(event.text)
            return SetNewMatchState(
                match=match,
                progress=SetNewMatchState.Progress.PLACE,
            )
        except:
            return SetNewMatchState(
                match=match,
                progress=SetNewMatchState.Progress.START_TIME_AGAIN,
            )
    elif (state.progress == SetNewMatchState.Progress.START_TIME_AGAIN) \
        and isinstance(event, MessageEvent):
        try:
            match.start_time = str_time_to_int(event.text)
            return SetNewMatchState(
                match=match,
                progress=SetNewMatchState.Progress.PLACE,
            )
        except:
            return SetNewMatchState(
                match=match,
                progress=SetNewMatchState.Progress.START_TIME_AGAIN,
            )
    elif (state.progress == SetNewMatchState.Progress.PLACE) \
        and isinstance(event, ButtonEvent):
        match.place_id = int(event.callback)
        return SetNewMatchState(
            match=match,
            progress=SetNewMatchState.Progress.GROUP,
        )
    elif (state.progress == SetNewMatchState.Progress.GROUP) \
        and isinstance(event, ButtonEvent):
        match.group_id = int(event.callback)
        return SetNewMatchState(
            match=match,
            progress=SetNewMatchState.Progress.GENRE,
        )
    elif (state.progress == SetNewMatchState.Progress.GENRE) \
        and isinstance(event, ButtonEvent):
        match.genre_id = int(event.callback)
        return SetNewMatchState(
            match=match,
            progress=SetNewMatchState.Progress.IS_LONELINESS_FRIENDLY,
        )
    elif (state.progress == SetNewMatchState.Progress.IS_LONELINESS_FRIENDLY) \
        and isinstance(event, ButtonEvent):
        match.is_loneliness_friendly = str_to_loneliness(event.callback)
        return SetNewMatchState(
            match=match,
            progress=SetNewMatchState.Progress.CONFIRMATION,
        )
    elif (state.progress == SetNewMatchState.Progress.CONFIRMATION) \
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


def on_veiw_by_place_state(state: VeiwByPlaceState, event: ButtonEvent):
    if event.callback == ButtonCallback.FILTERS:
        return FiltersState()
    if event.callback == ButtonCallback.SPECIAL_GO_BACK \
        and state.progress == VeiwByPlaceState.Progress.VEIW_FILTERED_BY_PLACE:
        return VeiwByPlaceState(
            item_id=0,
            match_id=0,
            progress=VeiwByPlaceState.Progress.VEIW_PLACES
        )
    if event.callback == ButtonCallback.SPECIAL_GO_BACK \
        and state.progress == VeiwByPlaceState.Progress.VEIW_ONE_FILTERED_BY_PLACE:
        return VeiwByPlaceState(
            item_id=state.item_id,
            match_id=0,
            progress=VeiwByPlaceState.Progress.VEIW_FILTERED_BY_PLACE
        )
    if state.progress == VeiwByPlaceState.Progress.VEIW_PLACES:
        return VeiwByPlaceState(
            item_id=event.callback,
            match_id=0,
            progress=VeiwByPlaceState.Progress.VEIW_FILTERED_BY_PLACE
        )
    if state.progress == VeiwByPlaceState.Progress.VEIW_FILTERED_BY_PLACE:
        return VeiwByPlaceState(
            item_id=state.item_id,
            match_id=event.callback,
            progress=VeiwByPlaceState.Progress.VEIW_ONE_FILTERED_BY_PLACE
        )


def on_veiw_by_group_state(state: VeiwByGroupState, event: ButtonEvent):
    if event.callback == ButtonCallback.FILTERS:
        return FiltersState()
    if event.callback == ButtonCallback.SPECIAL_GO_BACK \
        and state.progress == VeiwByGroupState.Progress.VEIW_FILTERED_BY_GROUP:
        return VeiwByGroupState(
            item_id=0,
            match_id=0,
            progress=VeiwByGroupState.Progress.VEIW_GROUPS
        )
    if event.callback == ButtonCallback.SPECIAL_GO_BACK \
        and state.progress == VeiwByGroupState.Progress.VEIW_ONE_FILTERED_BY_GROUP:
        return VeiwByGroupState(
            item_id=state.item_id,
            match_id=0,
            progress=VeiwByGroupState.Progress.VEIW_FILTERED_BY_GROUP
        )
    if state.progress == VeiwByGroupState.Progress.VEIW_GROUPS:
        return VeiwByGroupState(
            item_id=event.callback,
            match_id=0,
            progress=VeiwByGroupState.Progress.VEIW_FILTERED_BY_GROUP
        )
    if state.progress == VeiwByGroupState.Progress.VEIW_FILTERED_BY_GROUP:
        return VeiwByGroupState(
            item_id=state.item_id,
            match_id=event.callback,
            progress=VeiwByGroupState.Progress.VEIW_ONE_FILTERED_BY_GROUP
        )
    

def on_veiw_by_genre_state(state: VeiwByGenreState, event: ButtonEvent):
    if event.callback == ButtonCallback.FILTERS:
        return FiltersState()
    if event.callback == ButtonCallback.SPECIAL_GO_BACK \
        and state.progress == VeiwByGenreState.Progress.VEIW_FILTERED_BY_GENRE:
        return VeiwByGenreState(
            item_id=0,
            match_id=0,
            progress=VeiwByGenreState.Progress.VEIW_GENRES
        )
    if event.callback == ButtonCallback.SPECIAL_GO_BACK \
        and state.progress == VeiwByGenreState.Progress.VEIW_ONE_FILTERED_BY_GENRE:
        return VeiwByGenreState(
            item_id=state.item_id,
            match_id=0,
            progress=VeiwByGenreState.Progress.VEIW_FILTERED_BY_GENRE
        )
    if state.progress == VeiwByGenreState.Progress.VEIW_GENRES:
        return VeiwByGenreState(
            item_id=event.callback,
            match_id=0,
            progress=VeiwByGenreState.Progress.VEIW_FILTERED_BY_GENRE
        )
    if state.progress == VeiwByGenreState.Progress.VEIW_FILTERED_BY_GENRE:
        return VeiwByGenreState(
            item_id=state.item_id,
            match_id=event.callback,
            progress=VeiwByGenreState.Progress.VEIW_ONE_FILTERED_BY_GENRE
        )


def on_veiw_by_loneliness_state(state: VeiwByLonelinessState, event: ButtonEvent):
    if event.callback == ButtonCallback.FILTERS:
        return FiltersState()
    if event.callback == ButtonCallback.SPECIAL_GO_BACK \
        and state.progress == VeiwByLonelinessState.Progress.VEIW_FILTERED_BY_LONELINESS:
        return VeiwByLonelinessState(
            status=ButtonCallback.FALSE,
            match_id=0,
            progress=VeiwByLonelinessState.Progress.CHOOSE_LONELINESS_STATUS
        )
    if event.callback == ButtonCallback.SPECIAL_GO_BACK \
        and state.progress == VeiwByLonelinessState.Progress.VEIW_ONE_FILTERED_BY_LONELINESS:
        return VeiwByLonelinessState(
            status=state.status,
            match_id=0,
            progress=VeiwByLonelinessState.Progress.VEIW_FILTERED_BY_LONELINESS
        )
    if state.progress == VeiwByLonelinessState.Progress.CHOOSE_LONELINESS_STATUS:
        return VeiwByLonelinessState(
            status=event.callback,
            match_id=0,
            progress=VeiwByLonelinessState.Progress.VEIW_FILTERED_BY_LONELINESS
        )
    if state.progress == VeiwByLonelinessState.Progress.VEIW_FILTERED_BY_LONELINESS:
        return VeiwByLonelinessState(
            status=state.status,
            match_id=event.callback,
            progress=VeiwByLonelinessState.Progress.VEIW_ONE_FILTERED_BY_LONELINESS
        )
