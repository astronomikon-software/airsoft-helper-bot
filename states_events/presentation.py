from mapping.confirmation_mapping import str_to_bool
from mapping.datetime_mapping import int_time_to_str
from model.user import User
from states_events.states import *
from telebot import types

from states_events.menu_content.button_names import ButtonName
from states_events.menu_content.button_callbacks import ButtonCallback
from states_events.menu_content.message_texts import MessageText

from repository.repository_initiation import *

from utils.button_util import create_button


class ScreenPresentation:
    def __init__(self, markup, message_text):
        self.markup = markup
        self.message_text = message_text

    markup: types.InlineKeyboardMarkup
    message_text: str


def get_presentation(state: BotState, user: User) -> ScreenPresentation:
    if isinstance(state, MainMenuState):
        markup = types.InlineKeyboardMarkup()
        markup.add(
            create_button(
                text=ButtonName.SCHEDULE, 
                callback=ButtonCallback.SCHEDULE
            )
        )
        markup.add(
            create_button(
                text=ButtonName.HOW_TO,
                callback=ButtonCallback.HOW_TO
            )
        )
        markup.add(
            create_button(
                text=ButtonName.MARKET,
                callback=ButtonCallback.MARKET
            )
        )
        return ScreenPresentation(markup, MessageText.HELLO)
    
    elif isinstance(state, HowToState):
        markup = types.InlineKeyboardMarkup()
        markup.add(
            create_button(
                text=ButtonName.MAIN_MENU,
                callback=ButtonCallback.MAIN_MENU
            )
        )
        return ScreenPresentation(markup, MessageText.HOW_TO)
    
    elif isinstance(state, MarketState):
        markup = types.InlineKeyboardMarkup()
        markup.add(
            create_button(
                text=ButtonName.MAIN_MENU, 
                callback=ButtonCallback.MAIN_MENU
            )
        )
        return ScreenPresentation(markup, MessageText.MARKET)
    
    elif isinstance(state, ScheduleState):
        markup = types.InlineKeyboardMarkup()
        markup.add(
            create_button(
                text=ButtonName.CALENDAR, 
                callback=ButtonCallback.CALENDAR
            )
        )
        markup.add(
            create_button(
                text=ButtonName.FILTERS, 
                callback=ButtonCallback.FILTERS
            )
        )
        markup.add(
            create_button(
                text=ButtonName.ORGANISERS, 
                callback=ButtonCallback.ORGANISERS
            )
        )
        markup.add(
            create_button(
                text=ButtonName.GO_BACK, 
                callback=ButtonCallback.MAIN_MENU
            )
        )
        return ScreenPresentation(markup, MessageText.CHOOSE_FUNCTION)

    elif isinstance(state, OrganisersState):
        if user.is_admin:
            markup = types.InlineKeyboardMarkup()
            markup.add(
                create_button(
                    text=ButtonName.NEW_GAME,
                    callback=ButtonCallback.SET_DATETIME
                )
            )
            markup.add(
                create_button(
                    text=ButtonName.UPDATE_GAME,
                    callback=ButtonCallback.CHOOSE_GAME_TO_UPDATE
                )
            )
            if user.is_true_admin:
                markup.add(
                    create_button(
                        text=ButtonName.SET_ADMIN,
                        callback=ButtonCallback.SET_ADMIN
                    )
                )
            markup.add(
                create_button(
                    text=ButtonName.GO_BACK,
                    callback=ButtonCallback.SCHEDULE
                ),
                create_button(
                    text=ButtonName.MAIN_MENU, 
                    callback=ButtonCallback.MAIN_MENU
                )
            )
            return ScreenPresentation(markup, MessageText.CHOOSE_FUNCTION)
        else:
            markup = types.InlineKeyboardMarkup()
            markup.add(
                create_button(
                    text=ButtonName.GO_BACK,
                    callback=ButtonCallback.SCHEDULE
                ),
                create_button(
                    text=ButtonName.MAIN_MENU, 
                    callback=ButtonCallback.MAIN_MENU
                )
            )
            return ScreenPresentation(markup, MessageText.ORGANISER_APPLICATION)
        
    elif isinstance(state, EditMatchState):
        if state.progress == EditMatchState.Progress.START_TIME:
            markup = types.InlineKeyboardMarkup()
            return ScreenPresentation(markup, MessageText.SET_DATETIME)
        elif state.progress == EditMatchState.Progress.START_TIME_AGAIN:
            markup = types.InlineKeyboardMarkup()
            return ScreenPresentation(markup, MessageText.SET_DATETIME_AGAIN)
        elif state.progress == EditMatchState.Progress.PLACE:
            markup = types.InlineKeyboardMarkup()
            places = place_repository.read_all()
            for place in places:
                markup.add(
                    create_button(
                        text=place.name, 
                        callback=place.id
                    )
                )
            return ScreenPresentation(markup, MessageText.SET_PLACE)
        elif state.progress == EditMatchState.Progress.GROUP:
            markup = types.InlineKeyboardMarkup()
            groups = group_repository.read_all()
            for group in groups:
                markup.add(
                    create_button(
                        text=group.name, 
                        callback=group.id
                    )
                )
            return ScreenPresentation(markup, MessageText.SET_GROUP)
        elif state.progress == EditMatchState.Progress.GENRE:
            markup = types.InlineKeyboardMarkup()
            genres = genre_repository.read_all()
            for genre in genres:
                markup.add(
                    create_button(
                        text=genre.name, 
                        callback=genre.id
                    )
                )
            return ScreenPresentation(markup, MessageText.SET_GENRE)
        elif state.progress == EditMatchState.Progress.IS_LONELINESS_FRIENDLY:
            markup = types.InlineKeyboardMarkup()
            markup.add(
                create_button(
                    text=ButtonName.YES,
                    callback=ButtonCallback.TRUE
                ) 
            )
            markup.add(
                create_button(
                    text=ButtonName.NO,
                    callback=ButtonCallback.FALSE
                ) 
            )
            return ScreenPresentation(markup, MessageText.SET_LONELINESS)
        elif state.progress == EditMatchState.Progress.CONFIRMATION:
            markup = types.InlineKeyboardMarkup()
            markup.add(
                create_button(
                    text=ButtonName.SAVE_GAME,
                    callback=ButtonCallback.SAVE_GAME
                ) 
            )
            markup.add(
                create_button(
                    text=ButtonName.CANCEL_GAME_EDITING,
                    callback=ButtonCallback.CANCEL_GAME_EDITING
                ) 
            )
            return ScreenPresentation(markup, MessageText.CONFIRM_DATA + \
                '\n' + '\n' + MessageText.match_data(state.match))

    elif isinstance(state, GameIsSavedState):
        markup = types.InlineKeyboardMarkup()
        markup.add(
            create_button(
                text=ButtonName.BACK_TO_ORGANISERS, 
                callback=ButtonCallback.ORGANISERS
            )
        )
        markup.add(
            create_button(
                text=ButtonName.MAIN_MENU, 
                callback=ButtonCallback.MAIN_MENU
            )
        )
        return ScreenPresentation(markup, MessageText.NEW_GAME_CREATED)
    
    elif isinstance(state, GameIsCancelledState):
        markup = types.InlineKeyboardMarkup()
        markup.add(
            create_button(
                text=ButtonName.BACK_TO_ORGANISERS, 
                callback=ButtonCallback.ORGANISERS
            )
        ) 
        markup.add(
            create_button(
                text=ButtonName.MAIN_MENU, 
                callback=ButtonCallback.MAIN_MENU
            )
        )
        return ScreenPresentation(markup, MessageText.NEW_GAME_CANCELLED)

    elif isinstance(state, CalendarState):
        if state.progress == CalendarState.Progress.VEIW_ALL:
            markup = types.InlineKeyboardMarkup()
            matches = match_repository.read_all()
            matches.sort(key=lambda match: match.start_time)
            for match in matches:
                markup.add(
                    create_button(
                        text=ButtonName.small_match_data(match), 
                        callback=match.id
                    )
                )
            markup.add(
                create_button(
                    text=ButtonName.GO_BACK, 
                    callback=ButtonCallback.SCHEDULE
                ),
                create_button(
                    text=ButtonName.MAIN_MENU, 
                    callback=ButtonCallback.MAIN_MENU
                )
            )
            return ScreenPresentation(markup, MessageText.LIST_OF_MATCHES)
        elif state.progress == CalendarState.Progress.VEIW_ONE:
            markup = types.InlineKeyboardMarkup()
            match = match_repository.read(state.match_id)
            markup.add(
                create_button(
                    text=ButtonName.GO_BACK, 
                    callback=ButtonCallback.CALENDAR
                ),
                create_button(
                    text=ButtonName.MAIN_MENU, 
                    callback=ButtonCallback.MAIN_MENU
                )
            )
            return ScreenPresentation(markup, MessageText.match_data(match))

    elif isinstance(state, FiltersState):
        markup = types.InlineKeyboardMarkup()
        markup.add(
            create_button(
                text=ButtonName.PLACES, 
                callback=ButtonCallback.CHOOSE_PLACE
            )
        )
        markup.add(
            create_button(
                text=ButtonName.GROUPS, 
                callback=ButtonCallback.CHOOSE_GROUP
            )
        )
        markup.add(
            create_button(
                text=ButtonName.GENRES, 
                callback=ButtonCallback.CHOOSE_GENRE
            )
        )
        markup.add(
            create_button(
                text=ButtonName.LONELINESS, 
                callback=ButtonCallback.LONELINESS
            )
        )
        markup.add(
            create_button(
                text=ButtonName.GO_BACK, 
                callback=ButtonCallback.SCHEDULE
            ),
            create_button(
                text=ButtonName.MAIN_MENU, 
                callback=ButtonCallback.MAIN_MENU
            )
        )
        return ScreenPresentation(markup, MessageText.FILTERS)
    
    elif isinstance(state, VeiwByPlaceState):
        if state.progress == VeiwByPlaceState.Progress.VEIW_PLACES:
            markup = types.InlineKeyboardMarkup()
            places = place_repository.read_all()
            for place in places:
                markup.add(
                    create_button(
                        text=place.name, 
                        callback=place.id
                    )
                )
            markup.add(
                create_button(
                    text=ButtonName.GO_BACK, 
                    callback=ButtonCallback.FILTERS
                ),
                create_button(
                    text=ButtonName.MAIN_MENU, 
                    callback=ButtonCallback.MAIN_MENU
                )
            )
            return ScreenPresentation(markup, MessageText.CHOOSE_PLACE)
        elif state.progress == VeiwByPlaceState.Progress.VEIW_FILTERED_BY_PLACE:
            markup = types.InlineKeyboardMarkup()
            matches = match_repository.read_by_place(state.item_id)
            matches.sort(key=lambda match: match.start_time)
            for match in matches:
                markup.add(
                    create_button(
                        text=ButtonName.small_match_data(match), 
                        callback=match.id
                    )
                )
            markup.add(
                create_button(
                    text=ButtonName.GO_BACK, 
                    callback=ButtonCallback.SPECIAL_GO_BACK
                ),
                create_button(
                    text=ButtonName.MAIN_MENU, 
                    callback=ButtonCallback.MAIN_MENU
                )
            )
            return ScreenPresentation(markup, MessageText.LIST_OF_MATCHES)
        elif state.progress == VeiwByPlaceState.Progress.VEIW_ONE_FILTERED_BY_PLACE:
            markup = types.InlineKeyboardMarkup()
            match = match_repository.read(state.match_id)
            markup.add(
                create_button(
                    text=ButtonName.GO_BACK, 
                    callback=ButtonCallback.SPECIAL_GO_BACK
                ),
                create_button(
                    text=ButtonName.MAIN_MENU, 
                    callback=ButtonCallback.MAIN_MENU
                )
            )
            return ScreenPresentation(markup, MessageText.match_data(match))

    elif isinstance(state, VeiwByGroupState):
        if state.progress == VeiwByGroupState.Progress.VEIW_GROUPS:
            markup = types.InlineKeyboardMarkup()
            groups = group_repository.read_all()
            for group in groups:
                markup.add(
                    create_button(
                        text=group.name, 
                        callback=group.id
                    )
                )
            markup.add(
                create_button(
                    text=ButtonName.GO_BACK, 
                    callback=ButtonCallback.FILTERS
                ),
                create_button(
                    text=ButtonName.MAIN_MENU, 
                    callback=ButtonCallback.MAIN_MENU
                )
            )
            return ScreenPresentation(markup, MessageText.CHOOSE_GROUP)
        elif state.progress == VeiwByGroupState.Progress.VEIW_FILTERED_BY_GROUP:
            markup = types.InlineKeyboardMarkup()
            matches = match_repository.read_by_group(state.item_id)
            matches.sort(key=lambda match: match.start_time)
            for match in matches:
                markup.add(
                    create_button(
                        text=ButtonName.small_match_data(match), 
                        callback=match.id
                    )
                )
            markup.add(
                create_button(
                    text=ButtonName.GO_BACK, 
                    callback=ButtonCallback.SPECIAL_GO_BACK
                ),
                create_button(
                    text=ButtonName.MAIN_MENU, 
                    callback=ButtonCallback.MAIN_MENU
                )
            )
            return ScreenPresentation(markup, MessageText.LIST_OF_MATCHES)
        elif state.progress == VeiwByGroupState.Progress.VEIW_ONE_FILTERED_BY_GROUP:
            markup = types.InlineKeyboardMarkup()
            match = match_repository.read(state.match_id)
            markup.add(
                create_button(
                    text=ButtonName.GO_BACK, 
                    callback=ButtonCallback.SPECIAL_GO_BACK
                ),
                create_button(
                    text=ButtonName.MAIN_MENU, 
                    callback=ButtonCallback.MAIN_MENU
                )
            )
            return ScreenPresentation(markup, MessageText.match_data(match))

    elif isinstance(state, VeiwByGenreState):
        if state.progress == VeiwByGenreState.Progress.VEIW_GENRES:
            markup = types.InlineKeyboardMarkup()
            genres = genre_repository.read_all()
            for genre in genres:
                markup.add(
                    create_button(
                        text=genre.name, 
                        callback=genre.id
                    )
                )
            markup.add(
                create_button(
                    text=ButtonName.GO_BACK, 
                    callback=ButtonCallback.FILTERS
                ),
                create_button(
                    text=ButtonName.MAIN_MENU, 
                    callback=ButtonCallback.MAIN_MENU
                )
            )
            return ScreenPresentation(markup, MessageText.CHOOSE_GENRE)
        elif state.progress == VeiwByGenreState.Progress.VEIW_FILTERED_BY_GENRE:
            markup = types.InlineKeyboardMarkup()
            matches = match_repository.read_by_genre(state.item_id)
            matches.sort(key=lambda match: match.start_time)
            for match in matches:
                markup.add(
                    create_button(
                        text=ButtonName.small_match_data(match), 
                        callback=match.id
                    )
                )
            markup.add(
                create_button(
                    text=ButtonName.GO_BACK, 
                    callback=ButtonCallback.SPECIAL_GO_BACK
                ),
                create_button(
                    text=ButtonName.MAIN_MENU, 
                    callback=ButtonCallback.MAIN_MENU
                )
            )
            return ScreenPresentation(markup, MessageText.LIST_OF_MATCHES)
        elif state.progress == VeiwByGenreState.Progress.VEIW_ONE_FILTERED_BY_GENRE:
            markup = types.InlineKeyboardMarkup()
            match = match_repository.read(state.match_id)
            markup.add(
                create_button(
                    text=ButtonName.GO_BACK, 
                    callback=ButtonCallback.SPECIAL_GO_BACK
                ),
                create_button(
                    text=ButtonName.MAIN_MENU, 
                    callback=ButtonCallback.MAIN_MENU
                )
            )
            return ScreenPresentation(markup, MessageText.match_data(match))

    elif isinstance(state, VeiwByLonelinessState):
        if state.progress == VeiwByLonelinessState.Progress.CHOOSE_LONELINESS_STATUS:
            markup = types.InlineKeyboardMarkup()
            markup.add(
                create_button(
                    text=ButtonName.YES, 
                    callback=ButtonCallback.TRUE
                )
            )
            markup.add(
                create_button(
                    text=ButtonName.NO, 
                    callback=ButtonCallback.FALSE
                )
            )
            markup.add(
                create_button(
                    text=ButtonName.GO_BACK, 
                    callback=ButtonCallback.FILTERS
                ),
                create_button(
                    text=ButtonName.MAIN_MENU, 
                    callback=ButtonCallback.MAIN_MENU
                )
            )
            return ScreenPresentation(markup, MessageText.CHOOSE_LONELINESS_STATUS)
        elif state.progress == VeiwByLonelinessState.Progress.VEIW_FILTERED_BY_LONELINESS:
            markup = types.InlineKeyboardMarkup()
            matches = match_repository.read_by_loneliness(str_to_bool(state.status))
            matches.sort(key=lambda match: match.start_time)
            for match in matches:
                markup.add(
                    create_button(
                        text=ButtonName.small_match_data(match), 
                        callback=match.id
                    )
                )
            markup.add(
                create_button(
                    text=ButtonName.GO_BACK, 
                    callback=ButtonCallback.SPECIAL_GO_BACK
                ),
                create_button(
                    text=ButtonName.MAIN_MENU, 
                    callback=ButtonCallback.MAIN_MENU
                )
            )
            return ScreenPresentation(markup, MessageText.LIST_OF_MATCHES)
        elif state.progress == VeiwByLonelinessState.Progress.VEIW_ONE_FILTERED_BY_LONELINESS:
            markup = types.InlineKeyboardMarkup()
            match = match_repository.read(state.match_id)
            markup.add(
                create_button(
                    text=ButtonName.GO_BACK, 
                    callback=ButtonCallback.SPECIAL_GO_BACK
                ),
                create_button(
                    text=ButtonName.MAIN_MENU, 
                    callback=ButtonCallback.MAIN_MENU
                )
            )
            return ScreenPresentation(markup, MessageText.match_data(match))

        # YOU WERE HERE
    
    elif isinstance(state, UpdateMatchState):
        if state.progress == UpdateMatchState.Progress.CHOOSE_GAME:
            markup = types.InlineKeyboardMarkup()
            matches = match_repository.read_all()
            for match in matches:
                markup.add(
                    create_button(
                        text=ButtonName.small_match_data(match), 
                        callback=match.id
                    )
                )
            markup.add(
                create_button(
                    text=ButtonName.GO_BACK,
                    callback=ButtonCallback.ORGANISERS
                ),
                create_button(
                    text=ButtonName.MAIN_MENU, 
                    callback=ButtonCallback.MAIN_MENU
                )
            )
            return ScreenPresentation(markup, MessageText.LIST_OF_MATCHES)
        elif state.progress == UpdateMatchState.Progress.CONFIRM_UPDATING:
            match = match_repository.read(state.match_id)
            markup = types.InlineKeyboardMarkup()
            markup.add(
                create_button(
                    text=ButtonName.START_UPDATING,
                    callback=ButtonCallback.START_UPDATING
                )
            )
            markup.add(
                create_button(
                    text=ButtonName.GO_BACK,
                    callback=ButtonCallback.SPECIAL_GO_BACK
                ),
                create_button(
                    text=ButtonName.MAIN_MENU, 
                    callback=ButtonCallback.MAIN_MENU
                )
            )
            return ScreenPresentation(markup, MessageText.match_data(match))
        
        # YOU ARE HERE

    else:
        markup = types.InlineKeyboardMarkup()
        markup.add(
            create_button(
                text=ButtonName.MAIN_MENU, 
                callback=ButtonCallback.MAIN_MENU
            )
        )
        return ScreenPresentation(markup, 'Экран находится в разработке')
