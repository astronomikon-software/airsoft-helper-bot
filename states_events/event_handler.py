from model.user import User
from model.subscription import Subscription

from repository.repository_initiation import match_repository, subscription_repository

from states_events.menu_content.button_callbacks import ButtonCallback
from states_events.states import *
from states_events.events import *

from utils.datetime_util import check_datetime_format
from mapping.datetime_mapping import str_time_to_int, str_to_datetime
from mapping.loneliness_mapping import str_to_loneliness
from mapping.confirmation_mapping import str_to_confirmation


def get_new_state(state: BotState, event: BotEvent, user: User) -> BotState:
    if isinstance(event, ButtonEvent) and event.callback == ButtonCallback.MAIN_MENU:
        return MainMenuState()

    if isinstance(event, MessageEvent) and event.text == '/start':
        return MainMenuState()

    if isinstance(state, EditMatchState) and user.is_admin:
        return on_edit_match_state(state, event, user)

    if isinstance(state, CalendarState) and isinstance(event, ButtonEvent):
        return on_calendar_state(state, event)

    if isinstance(state, VeiwByPlaceState) and isinstance(event, ButtonEvent):
        return on_veiw_by_place_state(state, event)

    if isinstance(state, VeiwByGroupState) and isinstance(event, ButtonEvent):
        return on_veiw_by_group_state(state, event)

    if isinstance(state, VeiwByGenreState) and isinstance(event, ButtonEvent):
        return on_veiw_by_genre_state(state, event)
    
    if isinstance(state, VeiwByLonelinessState) and isinstance(event, ButtonEvent):
        return on_veiw_by_loneliness_state(state, event)
    
    if isinstance(state, VeiwByDateState) and isinstance(event, ButtonEvent):
        return on_veiw_by_date_state(state, event)
    
    if isinstance(state, UpdateMatchState) and user.is_admin:
        return on_update_match_state(state, event)
    
    if isinstance(state, SubscriptionState) and isinstance(event, ButtonEvent):
        return on_subscription_state(state, event, user)

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
            ButtonCallback.CHOOSE_DURATION: VeiwByDurationState,
            ButtonCallback.CHOOSE_DATE: VeiwByDateState,
            ButtonCallback.LONELINESS: VeiwByLonelinessState,
            ButtonCallback.ORGANISERS: OrganisersState,
            ButtonCallback.SET_DATETIME: EditMatchState,
            ButtonCallback.CALENDAR: CalendarState,
            ButtonCallback.CHOOSE_GAME_TO_UPDATE: UpdateMatchState,
            ButtonCallback.HELP: HelpState,
            ButtonCallback.SUBSCRIBE: SubscriptionState,
            ButtonCallback.DONATE: DonateState,
        }[event.callback]
        if state_class is not None:
            if state_class is EditMatchState:
                match = Match(
                id=0,
                name='',
                start_time=0,
                duration='',
                place_name=0,
                group_id=list(),
                genre_id=list(),
                is_loneliness_friendly=False,
                url='',
                annotation=''
                )
                return state_class(match=match, progress=EditMatchProgress.NAME)
            elif state_class is CalendarState:
                return state_class(match_id=0, page_number=1, progress=CalendarProgress.VEIW_ALL)
            elif state_class is VeiwByPlaceState:
                return state_class(0, 0, VeiwByPlaceProgress.VEIW_PLACES, 1)
            elif state_class is VeiwByGroupState:
                return state_class(0, 0, VeiwByGroupProgress.VEIW_GROUPS, 1)
            elif state_class is VeiwByGenreState:
                return state_class(0, 0, VeiwByGenreProgress.VEIW_GENRES, 1)
            elif state_class is VeiwByDateState:
                return state_class(VeiwByDateProgress.VEIW_DATES, 0, 0, 0)
            elif state_class is VeiwByLonelinessState:
                return state_class(ButtonCallback.FALSE, 0, VeiwByLonelinessProgress.CHOOSE_LONELINESS_STATUS, 1)
            elif state_class is UpdateMatchState:
                return UpdateMatchState(old_match=0, new_match=0, progress=UpdateMatchProgress.CHOOSE_GAME, page_number=1)
            elif state_class is SubscriptionState:
                try:
                    subscription = subscription_repository.read_by_user_id(user.id)
                    return state_class(is_subscribed=True)
                except:
                    return state_class(is_subscribed=False)
            else:
                return state_class()
    
    if isinstance(event, MessageEvent):
        if event.text == '/start':
            return MainMenuState()
        # elif event.text == some regexp 
    
        
def on_edit_match_state(state: EditMatchState, event: BotEvent, user: User):
    match = state.match
    if (state.progress == EditMatchProgress.NAME) \
        and isinstance(event, MessageEvent):
        match.name = event.text
        return EditMatchState(
            match=match,
            progress=EditMatchProgress.START_TIME,
        )
    elif (state.progress == EditMatchProgress.START_TIME) \
        and isinstance(event, MessageEvent):
        try:
            match.start_time = str_time_to_int(event.text)
            return EditMatchState(
                match=match,
                progress=EditMatchProgress.DURATION,
            )
        except:
            return EditMatchState(
                match=match,
                progress=EditMatchProgress.START_TIME_AGAIN,
            )
    elif (state.progress == EditMatchProgress.START_TIME_AGAIN) \
        and isinstance(event, MessageEvent):
        try:
            match.start_time = str_time_to_int(event.text)
            return EditMatchState(
                match=match,
                progress=EditMatchProgress.DURATION,
            )
        except:
            return EditMatchState(
                match=match,
                progress=EditMatchProgress.START_TIME_AGAIN,
            )
    elif (state.progress == EditMatchProgress.DURATION) \
        and isinstance(event, MessageEvent):
        match.duration = event.text
        return EditMatchState(
            match=match,
            progress=EditMatchProgress.PLACE,
        )
    elif (state.progress == EditMatchProgress.PLACE) \
        and isinstance(event, MessageEvent):
        match.place_name = event.text
        return EditMatchState(
            match=match,
            progress=EditMatchProgress.GROUP,
        )
    elif (state.progress == EditMatchProgress.GROUP) \
        and isinstance(event, ButtonEvent):
        if event.callback == ButtonCallback.NEXT_STEP:
            return EditMatchState(
                match=match,
                progress=EditMatchProgress.GENRE,
            )
        else:
            if int(event.callback) not in match.group_id:
                match.group_id.append(int(event.callback))
            else:
                match.group_id.remove(int(event.callback))
            return EditMatchState(
                match=match,
                progress=EditMatchProgress.GROUP,
            )
    elif (state.progress == EditMatchProgress.GENRE) \
        and isinstance(event, ButtonEvent):
        if event.callback == ButtonCallback.NEXT_STEP:
            return EditMatchState(
                match=match,
                progress=EditMatchProgress.IS_LONELINESS_FRIENDLY,
            )
        else:
            if int(event.callback) not in match.genre_id:
                match.genre_id.append(int(event.callback))
            else:
                match.genre_id.remove(int(event.callback))
            return EditMatchState(
                match=match,
                progress=EditMatchProgress.GENRE,
            )
    elif (state.progress == EditMatchProgress.IS_LONELINESS_FRIENDLY) \
        and isinstance(event, ButtonEvent):
        match.is_loneliness_friendly = str_to_loneliness(event.callback)
        return EditMatchState(
            match=match,
            progress=EditMatchProgress.URL,
        )
    elif (state.progress == EditMatchProgress.URL) \
        and isinstance(event, MessageEvent):
        match.url = event.text
        return EditMatchState(
            match=match,
            progress=EditMatchProgress.ANNOTATION,
        )
    elif (state.progress == EditMatchProgress.ANNOTATION) \
        and isinstance(event, MessageEvent):
        match.annotation = event.text
        return EditMatchState(
            match=match,
            progress=EditMatchProgress.CONFIRMATION,
        )
    elif (state.progress == EditMatchProgress.CONFIRMATION) \
        and isinstance(event, ButtonEvent):
        is_confirmed = str_to_confirmation(event.callback)
        if is_confirmed:
            if match.id != 0:
                match_repository.update(match)
                return GameIsUpdatedState()
            else:
                match_repository.create(match=match)
                return GameIsSavedState()
        else:
            return GameIsCancelledState()


def on_calendar_state(state: CalendarState, event: ButtonEvent):
    if event.callback == ButtonCallback.SCHEDULE:
        return ScheduleState()
    if event.callback == ButtonCallback.CALENDAR:
        return CalendarState(
            match_id=0,
            page_number=0,
            progress=CalendarProgress.VEIW_ALL,
        )
    if event.callback == ButtonCallback.SPECIAL_GO_BACK \
        and state.progress == CalendarProgress.VEIW_ONE:
        return CalendarState(
            match_id=0,
            page_number=state.page_number,
            progress=CalendarProgress.VEIW_ALL
        )
    if event.callback == ButtonCallback.NEXT_PAGE:
        return CalendarState(
            match_id=0,
            page_number=state.page_number+1,
            progress=CalendarProgress.VEIW_ALL
        )
    if event.callback == ButtonCallback.PREVIOUS_PAGE:
        return CalendarState(
            match_id=0,
            page_number=state.page_number-1,
            progress=CalendarProgress.VEIW_ALL
        )
    # if event.callback == ButtonCallback.VOID \
    #     and state.progress == CalendarProgress.VEIW_ALL: # Шутка юмора. Но я не знаю, что тут ещё придумать
    #     print(event.callback)
    #     print('may the void be with you eternally')
    if state.progress == CalendarProgress.VEIW_ALL:
        return CalendarState(
            match_id=int(event.callback),
            page_number=state.page_number,
            progress=CalendarProgress.VEIW_ONE
        )


def on_veiw_by_place_state(state: VeiwByPlaceState, event: ButtonEvent):
    if event.callback == ButtonCallback.FILTERS:
        return FiltersState()
    if event.callback == ButtonCallback.SPECIAL_GO_BACK \
        and state.progress == VeiwByPlaceProgress.VEIW_FILTERED_BY_PLACE:
        return VeiwByPlaceState(
            item_id=0,
            match_id=0,
            page_number=0,
            progress=VeiwByPlaceProgress.VEIW_PLACES
        )
    if event.callback == ButtonCallback.SPECIAL_GO_BACK \
        and state.progress == VeiwByPlaceProgress.VEIW_ONE_FILTERED_BY_PLACE:
        return VeiwByPlaceState(
            item_id=state.place_name,
            match_id=0,
            page_number=state.page_number,
            progress=VeiwByPlaceProgress.VEIW_FILTERED_BY_PLACE
        )
    if event.callback == ButtonCallback.NEXT_PAGE:
        return VeiwByPlaceState(
            item_id=state.place_name,
            match_id=0,
            page_number=state.page_number+1,
            progress=VeiwByPlaceProgress.VEIW_FILTERED_BY_PLACE
        )
    if event.callback == ButtonCallback.PREVIOUS_PAGE:
        return VeiwByPlaceState(
            item_id=state.place_name,
            match_id=0,
            page_number=state.page_number-1,
            progress=VeiwByPlaceProgress.VEIW_FILTERED_BY_PLACE
        )
    if state.progress == VeiwByPlaceProgress.VEIW_PLACES:
        return VeiwByPlaceState(
            item_id=event.callback,
            match_id=0,
            page_number=1,
            progress=VeiwByPlaceProgress.VEIW_FILTERED_BY_PLACE
        )
    if state.progress == VeiwByPlaceProgress.VEIW_FILTERED_BY_PLACE:
        return VeiwByPlaceState(
            item_id=state.place_name,
            match_id=event.callback,
            page_number=state.page_number,
            progress=VeiwByPlaceProgress.VEIW_ONE_FILTERED_BY_PLACE
        )


def on_veiw_by_group_state(state: VeiwByGroupState, event: ButtonEvent):
    if event.callback == ButtonCallback.FILTERS:
        return FiltersState()
    if event.callback == ButtonCallback.SPECIAL_GO_BACK \
        and state.progress == VeiwByGroupProgress.VEIW_FILTERED_BY_GROUP:
        return VeiwByGroupState(
            item_id=0,
            match_id=0,
            page_number=0,
            progress=VeiwByGroupProgress.VEIW_GROUPS
        )
    if event.callback == ButtonCallback.SPECIAL_GO_BACK \
        and state.progress == VeiwByGroupProgress.VEIW_ONE_FILTERED_BY_GROUP:
        return VeiwByGroupState(
            item_id=state.item_id,
            match_id=0,
            page_number=state.page_number,
            progress=VeiwByGroupProgress.VEIW_FILTERED_BY_GROUP
        )
    if event.callback == ButtonCallback.NEXT_PAGE:
        return VeiwByGroupState(
            item_id=state.item_id,
            match_id=0,
            page_number=state.page_number+1,
            progress=VeiwByGroupProgress.VEIW_FILTERED_BY_GROUP
        )
    if event.callback == ButtonCallback.PREVIOUS_PAGE:
        return VeiwByGroupState(
            item_id=state.item_id,
            match_id=0,
            page_number=state.page_number-1,
            progress=VeiwByGroupProgress.VEIW_FILTERED_BY_GROUP
        )
    if state.progress == VeiwByGroupProgress.VEIW_GROUPS:
        return VeiwByGroupState(
            item_id=event.callback,
            match_id=0,
            page_number=1,
            progress=VeiwByGroupProgress.VEIW_FILTERED_BY_GROUP
        )
    if state.progress == VeiwByGroupProgress.VEIW_FILTERED_BY_GROUP:
        return VeiwByGroupState(
            item_id=state.item_id,
            match_id=event.callback,
            page_number=state.page_number,
            progress=VeiwByGroupProgress.VEIW_ONE_FILTERED_BY_GROUP
        )
    

def on_veiw_by_genre_state(state: VeiwByGenreState, event: ButtonEvent):
    if event.callback == ButtonCallback.FILTERS:
        return FiltersState()
    if event.callback == ButtonCallback.SPECIAL_GO_BACK \
        and state.progress == VeiwByGenreProgress.VEIW_FILTERED_BY_GENRE:
        return VeiwByGenreState(
            item_id=0,
            match_id=0,
            page_number=0,
            progress=VeiwByGenreProgress.VEIW_GENRES
        )
    if event.callback == ButtonCallback.SPECIAL_GO_BACK \
        and state.progress == VeiwByGenreProgress.VEIW_ONE_FILTERED_BY_GENRE:
        return VeiwByGenreState(
            item_id=state.item_id,
            match_id=0,
            page_number=state.page_number,
            progress=VeiwByGenreProgress.VEIW_FILTERED_BY_GENRE
        )
    if event.callback == ButtonCallback.NEXT_PAGE:
        return VeiwByGenreState(
            item_id=state.item_id,
            match_id=0,
            page_number=state.page_number+1,
            progress=VeiwByGenreProgress.VEIW_FILTERED_BY_GENRE
        )
    if event.callback == ButtonCallback.PREVIOUS_PAGE:
        return VeiwByGenreState(
            item_id=state.item_id,
            match_id=0,
            page_number=state.page_number-1,
            progress=VeiwByGenreProgress.VEIW_FILTERED_BY_GENRE
        )
    if state.progress == VeiwByGenreProgress.VEIW_GENRES:
        return VeiwByGenreState(
            item_id=event.callback,
            match_id=0,
            page_number=1,
            progress=VeiwByGenreProgress.VEIW_FILTERED_BY_GENRE
        )
    if state.progress == VeiwByGenreProgress.VEIW_FILTERED_BY_GENRE:
        return VeiwByGenreState(
            item_id=state.item_id,
            match_id=event.callback,
            page_number=state.page_number,
            progress=VeiwByGenreProgress.VEIW_ONE_FILTERED_BY_GENRE
        )


def on_veiw_by_loneliness_state(state: VeiwByLonelinessState, event: ButtonEvent):
    if event.callback == ButtonCallback.FILTERS:
        return FiltersState()
    if event.callback == ButtonCallback.SPECIAL_GO_BACK \
        and state.progress == VeiwByLonelinessProgress.VEIW_FILTERED_BY_LONELINESS:
        return VeiwByLonelinessState(
            status=ButtonCallback.FALSE,
            match_id=0,
            page_number=0,
            progress=VeiwByLonelinessProgress.CHOOSE_LONELINESS_STATUS
        )
    if event.callback == ButtonCallback.SPECIAL_GO_BACK \
        and state.progress == VeiwByLonelinessProgress.VEIW_ONE_FILTERED_BY_LONELINESS:
        return VeiwByLonelinessState(
            status=state.status,
            match_id=0,
            page_number=state.page_number,
            progress=VeiwByLonelinessProgress.VEIW_FILTERED_BY_LONELINESS
        )
    if event.callback == ButtonCallback.NEXT_PAGE:
        return VeiwByLonelinessState(
            status=state.status,
            match_id=0,
            page_number=state.page_number+1,
            progress=VeiwByLonelinessProgress.VEIW_FILTERED_BY_LONELINESS
        )
    if event.callback == ButtonCallback.PREVIOUS_PAGE:
        return VeiwByLonelinessState(
            status=state.status,
            match_id=0,
            page_number=state.page_number-1,
            progress=VeiwByLonelinessProgress.VEIW_FILTERED_BY_LONELINESS
        )
    if state.progress == VeiwByLonelinessProgress.CHOOSE_LONELINESS_STATUS:
        return VeiwByLonelinessState(
            status=str_to_loneliness(event.callback),
            match_id=0,
            page_number=1,
            progress=VeiwByLonelinessProgress.VEIW_FILTERED_BY_LONELINESS
        )
    if state.progress == VeiwByLonelinessProgress.VEIW_FILTERED_BY_LONELINESS:
        return VeiwByLonelinessState(
            status=state.status,
            match_id=event.callback,
            page_number=state.page_number,
            progress=VeiwByLonelinessProgress.VEIW_ONE_FILTERED_BY_LONELINESS
        )


def on_veiw_by_date_state(state: VeiwByDateState, event: ButtonEvent):
    if state.progress == VeiwByDateProgress.VEIW_DATES: # решил оформление по условиям слегка поменять
        if event.callback == ButtonCallback.FILTERS:
            return FiltersState()       
        if event.callback == ButtonCallback.NEXT_MONTH:
            return VeiwByDateState(
                progress=VeiwByDateProgress.VEIW_DATES,
                month_offset=state.month_offset+1,
                date=state.date,
                match_id=state.match_id
            )
        if event.callback == ButtonCallback.PREVIOUS_MONTH:
            return VeiwByDateState(
                progress=VeiwByDateProgress.VEIW_DATES,
                month_offset=state.month_offset-1,
                date=state.date,
                match_id=state.match_id
            )
        # if event.callback == ButtonCallback.VOID:
        #     return state
        else:
            return VeiwByDateState(
                progress=VeiwByDateProgress.VEIW_FILTERED_BY_DATE,
                month_offset=state.month_offset,
                date=int(event.callback),
                match_id=state.match_id
            )
    if state.progress == VeiwByDateProgress.VEIW_FILTERED_BY_DATE:
        if event.callback == ButtonCallback.SPECIAL_GO_BACK:
            return VeiwByDateState(
                progress=VeiwByDateProgress.VEIW_DATES,
                month_offset=state.month_offset,
                date=state.date,
                match_id=state.match_id
            )
        else:
            return VeiwByDateState(
                progress=VeiwByDateProgress.VEIW_ONE_FILTERED_BY_DATE,
                month_offset=state.month_offset,
                date=state.date,
                match_id=int(event.callback)
            )
    if state.progress == VeiwByDateProgress.VEIW_ONE_FILTERED_BY_DATE \
        and event.callback == ButtonCallback.SPECIAL_GO_BACK:
        return VeiwByDateState(
                progress=VeiwByDateProgress.VEIW_FILTERED_BY_DATE,
                month_offset=state.month_offset,
                date=state.date,
                match_id=state.match_id
            )


# Вспоминаются времена, когда я лежал в больнице. Как я гулял по территории. Как ждал Анну. Мне её очень не хватает.


def on_update_match_state(state: UpdateMatchState, event: ButtonEvent):
    if state.progress == UpdateMatchProgress.CHOOSE_GAME \
        and event.callback == ButtonCallback.ORGANISERS:
        return OrganisersState()
    elif state.progress == UpdateMatchProgress.CONFIRM_UPDATING \
        and event.callback == ButtonCallback.SPECIAL_GO_BACK:
        return UpdateMatchState(
            old_match=0,
            new_match=0,
            progress=UpdateMatchProgress.CHOOSE_GAME,
            page_number=state.page_number
        )
    elif state.progress == UpdateMatchProgress.CHOOSE_GAME \
        and event.callback == ButtonCallback.NEXT_PAGE:
        return UpdateMatchState(
            old_match=0,
            new_match=0,
            progress=UpdateMatchProgress.CHOOSE_GAME,
            page_number=state.page_number+1,
        )
    elif state.progress == UpdateMatchProgress.CHOOSE_GAME \
        and event.callback == ButtonCallback.PREVIOUS_PAGE:
        return UpdateMatchState(
            old_match=0,
            new_match=0,
            progress=UpdateMatchProgress.CHOOSE_GAME,
            page_number=state.page_number-1,
        )
    elif state.progress == UpdateMatchProgress.CHOOSE_GAME:
        return UpdateMatchState(
            old_match=match_repository.read(event.callback),
            new_match=match_repository.read(event.callback),
            progress=UpdateMatchProgress.CONFIRM_UPDATING,
            page_number=state.page_number,
        )
    elif state.progress == UpdateMatchProgress.CONFIRM_UPDATING \
        and event.callback == ButtonCallback.START_UPDATING:
        return UpdateMatchState(
            old_match=state.old_match,
            new_match=state.new_match,
            progress=UpdateMatchProgress.COMPARING_EDITIONS,
            page_number=1,
        )
    elif state.progress == UpdateMatchProgress.UPDATE_NAME \
        and isinstance(event, MessageEvent):
        updating_match = state.new_match
        updating_match.name = event.text
        return UpdateMatchState(
            old_match=state.old_match,
            new_match=updating_match,
            progress=UpdateMatchProgress.COMPARING_EDITIONS,
            page_number=1,
        )
    elif state.progress == UpdateMatchProgress.UPDATE_START_TIME \
        and isinstance(event, MessageEvent):
        try:
            updating_match = state.new_match
            updating_match.start_time = str_time_to_int(event.text)
            return UpdateMatchState(
                old_match=state.old_match,
                new_match=updating_match,
                progress=UpdateMatchProgress.COMPARING_EDITIONS,
                page_number=1,
            )
        except:
            return UpdateMatchState(
                old_match=state.old_match,
                new_match=state.new_match,
                progress=UpdateMatchProgress.UPDATE_START_TIME_AGAIN,
                page_number=1,
            )
    elif state.progress == UpdateMatchProgress.UPDATE_START_TIME_AGAIN \
        and isinstance(event, MessageEvent):
        try:
            updating_match = state.new_match
            updating_match.start_time = str_time_to_int(event.text)
            return UpdateMatchState(
                old_match=state.old_match,
                new_match=updating_match,
                progress=UpdateMatchProgress.COMPARING_EDITIONS,
                page_number=1,
            )
        except:
            return UpdateMatchState(
                old_match=state.old_match,
                new_match=state.new_match,
                progress=UpdateMatchProgress.UPDATE_START_TIME_AGAIN,
                page_number=1,
            )
    elif state.progress == UpdateMatchProgress.UPDATE_DURATION \
        and isinstance(event, MessageEvent):
        updating_match = state.new_match
        updating_match.duration = event.text
        return UpdateMatchState(
            old_match=state.old_match,
            new_match=updating_match,
            progress=UpdateMatchProgress.COMPARING_EDITIONS,
            page_number=1,
        )
    elif state.progress == UpdateMatchProgress.UPDATE_PLACE \
        and isinstance(event, MessageEvent):
        updating_match = state.new_match
        updating_match.place_name = event.text
        return UpdateMatchState(
            old_match=state.old_match,
            new_match=updating_match,
            progress=UpdateMatchProgress.COMPARING_EDITIONS,
            page_number=1,
        )
    elif state.progress == UpdateMatchProgress.UPDATE_GROUP \
        and isinstance(event, ButtonEvent):
        updating_match = state.new_match
        if event.callback == ButtonCallback.NEXT_STEP:
            return UpdateMatchState(
                old_match=state.old_match,
                new_match=updating_match,
                progress=UpdateMatchProgress.COMPARING_EDITIONS,
                page_number=1,
            )
        else:
            if int(event.callback) not in updating_match.group_id:
                updating_match.group_id.append(int(event.callback))
            else:
                updating_match.group_id.remove(int(event.callback))
            return UpdateMatchState(
                old_match=state.old_match,
                new_match=updating_match,
                progress=UpdateMatchProgress.UPDATE_GROUP,
                page_number=1,
            )
    elif state.progress == UpdateMatchProgress.UPDATE_GENRE \
        and isinstance(event, ButtonEvent):
        updating_match = state.new_match
        if event.callback == ButtonCallback.NEXT_STEP:
            return UpdateMatchState(
                old_match=state.old_match,
                new_match=updating_match,
                progress=UpdateMatchProgress.COMPARING_EDITIONS,
                page_number=1,
            )
        else:
            if int(event.callback) not in updating_match.genre_id:
                updating_match.genre_id.append(int(event.callback))
            else:
                updating_match.genre_id.remove(int(event.callback))
            return UpdateMatchState(
                old_match=state.old_match,
                new_match=updating_match,
                progress=UpdateMatchProgress.UPDATE_GENRE,
                page_number=1,
            )
    elif state.progress == UpdateMatchProgress.UPDATE_LONELINESS \
        and isinstance(event, ButtonEvent):
        updating_match = state.new_match
        updating_match.is_loneliness_friendly = str_to_loneliness(event.callback)
        return UpdateMatchState(
            old_match=state.old_match,
            new_match=state.new_match,
            progress=UpdateMatchProgress.COMPARING_EDITIONS,
            page_number=1,
        )
    elif state.progress == UpdateMatchProgress.UPDATE_URL \
        and isinstance(event, MessageEvent):
        updating_match = state.new_match
        updating_match.url = event.text
        return UpdateMatchState(
            old_match=state.old_match,
            new_match=state.new_match,
            progress=UpdateMatchProgress.COMPARING_EDITIONS,
            page_number=1,
        )
    elif state.progress == UpdateMatchProgress.UPDATE_ANNOTATION \
        and isinstance(event, MessageEvent):
        updating_match = state.new_match
        updating_match.annotation = event.text
        return UpdateMatchState(
            old_match=state.old_match,
            new_match=state.new_match,
            progress=UpdateMatchProgress.COMPARING_EDITIONS,
            page_number=1,
        )
    elif state.progress == UpdateMatchProgress.COMPARING_EDITIONS \
        and event.callback == ButtonCallback.UPDATE_NAME:
        return UpdateMatchState(
            old_match=state.old_match,
            new_match=state.new_match,
            progress=UpdateMatchProgress.UPDATE_NAME,
            page_number=1,
        )
    elif state.progress == UpdateMatchProgress.COMPARING_EDITIONS \
        and event.callback == ButtonCallback.UPDATE_START_TIME:
        return UpdateMatchState(
            old_match=state.old_match,
            new_match=state.new_match,
            progress=UpdateMatchProgress.UPDATE_START_TIME,
            page_number=1,
        )
    elif state.progress == UpdateMatchProgress.COMPARING_EDITIONS \
        and event.callback == ButtonCallback.UPDATE_DURATION:
        return UpdateMatchState(
            old_match=state.old_match,
            new_match=state.new_match,
            progress=UpdateMatchProgress.UPDATE_DURATION,
            page_number=1,
        )
    elif state.progress == UpdateMatchProgress.COMPARING_EDITIONS \
        and event.callback == ButtonCallback.UPDATE_PLACE:
        return UpdateMatchState(
            old_match=state.old_match,
            new_match=state.new_match,
            progress=UpdateMatchProgress.UPDATE_PLACE,
            page_number=1,
        )
    elif state.progress == UpdateMatchProgress.COMPARING_EDITIONS \
        and event.callback == ButtonCallback.UPDATE_GROUP:
        new_match = state.new_match
        new_match.group_id = list()
        return UpdateMatchState(
            old_match=state.old_match,
            new_match=new_match,
            progress=UpdateMatchProgress.UPDATE_GROUP,
            page_number=1,
        )
    elif state.progress == UpdateMatchProgress.COMPARING_EDITIONS \
        and event.callback == ButtonCallback.UPDATE_GENRE:
        new_match = state.new_match
        new_match.genre_id = list()
        return UpdateMatchState(
            old_match=state.old_match,
            new_match=new_match,
            progress=UpdateMatchProgress.UPDATE_GENRE,
            page_number=1,
        )
    elif state.progress == UpdateMatchProgress.COMPARING_EDITIONS \
        and event.callback == ButtonCallback.UPDATE_LONELINESS:
        return UpdateMatchState(
            old_match=state.old_match,
            new_match=state.new_match,
            progress=UpdateMatchProgress.UPDATE_LONELINESS,
            page_number=1,
        )
    elif state.progress == UpdateMatchProgress.COMPARING_EDITIONS \
        and event.callback == ButtonCallback.UPDATE_URL:
        return UpdateMatchState(
            old_match=state.old_match,
            new_match=state.new_match,
            progress=UpdateMatchProgress.UPDATE_URL,
            page_number=1,
        )
    elif state.progress == UpdateMatchProgress.COMPARING_EDITIONS \
        and event.callback == ButtonCallback.UPDATE_ANNOTATION:
        return UpdateMatchState(
            old_match=state.old_match,
            new_match=state.new_match,
            progress=UpdateMatchProgress.UPDATE_ANNOTATION,
            page_number=1,
        )
    elif state.progress == UpdateMatchProgress.COMPARING_EDITIONS \
        and event.callback == ButtonCallback.CANCEL_GAME_EDITING:
        return GameUpdatingIsCancelledState()
    elif state.progress == UpdateMatchProgress.COMPARING_EDITIONS \
        and event.callback == ButtonCallback.SAVE_GAME:
        match_repository.update(state.new_match)
        return GameIsUpdatedState()


def on_subscription_state(state: SubscriptionState, event: ButtonEvent, user: User):
    if event.callback == ButtonCallback.CREATE_SUBSCRIPTION:
        subscription = Subscription()
        subscription.user_id = user.id
        subscription_repository.create(subscription)
        return SubscriptionManagedState(is_created=True)
    elif event.callback == ButtonCallback.DELETE_SUBSCRIPTION:
        subscription = subscription_repository.read_by_user_id(user.id)
        subscription_repository.delete(subscription)
        return SubscriptionManagedState(is_created=False)
