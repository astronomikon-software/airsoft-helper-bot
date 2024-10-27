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
from utils.paging_util import add_navigation


class ScreenPresentation:
    def __init__(self, markup, message_text):
        self.markup = markup
        self.message_text = message_text

    markup: types.InlineKeyboardMarkup
    message_text: str


def get_presentation(state: BotState, user: User) -> ScreenPresentation:
    if isinstance(state, MainMenuState):
        return main_menu_presentation(state)
    
    elif isinstance(state, HowToState):
        return how_to_presentation(state)
    
    elif isinstance(state, MarketState):
        return market_presentation(state)
    
    elif isinstance(state, ScheduleState):
        return schedule_presentation(state)
    
    elif isinstance(state, HelpState):
        return help_presentation(state)

    elif isinstance(state, OrganisersState):
        return organisers_presentation(state, user)
    
    elif isinstance(state, EditMatchState):
        return edit_match_presentation(state)

    elif isinstance(state, GameIsSavedState):
        return game_is_saved_presentation(state)
    
    elif isinstance(state, GameIsCancelledState):
        return game_is_cancelled_presentation(state)

    elif isinstance(state, CalendarState):
        return calendar_presentation(state)

    elif isinstance(state, FiltersState):
        return filters_presentation(state)
    
    elif isinstance(state, VeiwByPlaceState):
        return veiw_by_place_presentation(state)

    elif isinstance(state, VeiwByGroupState):
        return veiw_by_group_presentation(state)

    elif isinstance(state, VeiwByGenreState):
        return veiw_by_genre_presentation(state)

    elif isinstance(state, VeiwByLonelinessState):
        return veiw_by_loneliness_presentation(state)
    
    elif isinstance(state, UpdateMatchState):
        return update_match_presentation(state)
        
    elif isinstance(state, GameIsUpdatedState):
        return game_is_updated_presentation(state)
    
    elif isinstance(state, GameUpdatingIsCancelledState):
        return game_updating_is_cancelled_presentation(state)
    
    elif isinstance(state, SubscriptionState):
        return subscribtion_presentation(state)
    
    elif isinstance(state, SubscriptionManagedState):
        return subscribtion_managed_presentation(state)

    else:
        return error_presentation(state)


def main_menu_presentation(state: MainMenuState):
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
    markup.add(
        create_button(
            text=ButtonName.HELP,
            callback=ButtonCallback.HELP
        )
    )
    return ScreenPresentation(markup, MessageText.HELLO)


def how_to_presentation(state: HowToState):
    markup = types.InlineKeyboardMarkup()
    markup.add(
        create_button(
            text=ButtonName.MAIN_MENU,
            callback=ButtonCallback.MAIN_MENU
        )
    )
    return ScreenPresentation(markup, MessageText.HOW_TO)


def market_presentation(state: MarketState):
    markup = types.InlineKeyboardMarkup()
    markup.add(
        create_button(
            text=ButtonName.MAIN_MENU, 
            callback=ButtonCallback.MAIN_MENU
        )
    )
    return ScreenPresentation(markup, MessageText.MARKET)


def help_presentation(state: HelpState):
    markup = types.InlineKeyboardMarkup()
    markup.add(
        create_button(
            text=ButtonName.MAIN_MENU, 
            callback=ButtonCallback.MAIN_MENU
        )
    )
    return ScreenPresentation(markup, MessageText.HELP)


def schedule_presentation(state: ScheduleState):
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
            text=ButtonName.SUBSCRIBE, 
            callback=ButtonCallback.SUBSCRIBE
        )
    )
    markup.add(
        create_button(
            text=ButtonName.GO_BACK, 
            callback=ButtonCallback.MAIN_MENU
        )
    )
    return ScreenPresentation(markup, MessageText.SCHEDULE)


def organisers_presentation(state, user: User):
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


def edit_match_presentation(state: EditMatchState):
    if state.progress == EditMatchProgress.NAME:
        markup = types.InlineKeyboardMarkup()
        return ScreenPresentation(markup, MessageText.SET_NAME)
    elif state.progress == EditMatchProgress.START_TIME:
        markup = types.InlineKeyboardMarkup()
        return ScreenPresentation(markup, MessageText.SET_DATETIME)
    elif state.progress == EditMatchProgress.START_TIME_AGAIN:
        markup = types.InlineKeyboardMarkup()
        return ScreenPresentation(markup, MessageText.SET_DATETIME_AGAIN)
    elif state.progress == EditMatchProgress.PLACE:
        markup = types.InlineKeyboardMarkup()
        return ScreenPresentation(markup, MessageText.SET_PLACE)
    elif state.progress == EditMatchProgress.GROUP:
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
    elif state.progress == EditMatchProgress.GENRE:
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
    elif state.progress == EditMatchProgress.IS_LONELINESS_FRIENDLY:
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
    if state.progress == EditMatchProgress.URL:
        markup = types.InlineKeyboardMarkup()
        return ScreenPresentation(markup, MessageText.SET_URL)
    elif state.progress == EditMatchProgress.CONFIRMATION:
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


def game_is_saved_presentation(state: GameIsSavedState):
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


def game_is_cancelled_presentation(state: GameIsCancelledState):
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


def calendar_presentation(state: CalendarState):
    if state.progress == CalendarProgress.VEIW_ALL:
        markup = types.InlineKeyboardMarkup()
        page_size = 8
        matches = match_repository.read_ongoing(limit=page_size, offset=((state.page_number - 1) * page_size))
        
        for match in matches:
            markup.add(
                create_button(
                    text=ButtonName.small_match_data(match), 
                    callback=match.id
                )
            )
        markup = add_navigation(
            markup=markup,
            page_size=page_size,
            page_number=state.page_number,
            number_of_matches=match_repository.count_all_ongoings()
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
    elif state.progress == CalendarProgress.VEIW_ONE:
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


def filters_presentation(state: FiltersState):
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


def veiw_by_place_presentation(state: VeiwByPlaceState):
    if state.progress == VeiwByPlaceProgress.VEIW_PLACES:
        markup = types.InlineKeyboardMarkup()
        places = place_repository.read_all()
        for place in places:
            markup.add(
                create_button(
                    text=place, 
                    callback=place
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
    elif state.progress == VeiwByPlaceProgress.VEIW_FILTERED_BY_PLACE:
        markup = types.InlineKeyboardMarkup()
        page_size = 8
        matches = match_repository.read_by_place(
            place_name=state.item_id, 
            limit=page_size, 
            offset=((state.page_number - 1) * page_size)
        )

        if len(matches) == 0:
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
            return ScreenPresentation(markup, MessageText.NO_MATCHES_FOUND)
        elif len(matches) > 0:
            for match in matches:
                markup.add(
                    create_button(
                        text=ButtonName.small_match_data(match), 
                        callback=match.id
                    )
                )
            markup = add_navigation(
                markup=markup,
                page_size=page_size,
                page_number=state.page_number,
                number_of_matches=match_repository.count_by_place(state.item_id)
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
    elif state.progress == VeiwByPlaceProgress.VEIW_ONE_FILTERED_BY_PLACE:
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


def veiw_by_group_presentation(state: VeiwByGroupState):
    if state.progress == VeiwByGroupProgress.VEIW_GROUPS:
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
    elif state.progress == VeiwByGroupProgress.VEIW_FILTERED_BY_GROUP:
        markup = types.InlineKeyboardMarkup()
        page_size = 8
        matches = match_repository.read_by_group(
            group_id=state.item_id,
            limit=page_size, 
            offset=((state.page_number - 1) * page_size)
        )
        if len(matches) == 0:
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
            return ScreenPresentation(markup, MessageText.NO_MATCHES_FOUND)
        elif len(matches) > 0:
            for match in matches:
                markup.add(
                    create_button(
                        text=ButtonName.small_match_data(match), 
                        callback=match.id
                    )
                )
            markup = add_navigation(
                markup=markup,
                page_size=page_size,
                page_number=state.page_number,
                number_of_matches=match_repository.count_by_group(state.item_id)
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
    elif state.progress == VeiwByGroupProgress.VEIW_ONE_FILTERED_BY_GROUP:
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


def veiw_by_genre_presentation(state: VeiwByGenreState):
    if state.progress == VeiwByGenreProgress.VEIW_GENRES:
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
    elif state.progress == VeiwByGenreProgress.VEIW_FILTERED_BY_GENRE:
        markup = types.InlineKeyboardMarkup()
        page_size = 8
        matches = match_repository.read_by_genre(
            genre_id=state.item_id,
            limit=page_size, 
            offset=((state.page_number - 1) * page_size)
        )

        if len(matches) == 0:
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
            return ScreenPresentation(markup, MessageText.NO_MATCHES_FOUND)
        elif len(matches) > 0:
            for match in matches:
                markup.add(
                    create_button(
                        text=ButtonName.small_match_data(match), 
                        callback=match.id
                    )
                )
            markup = add_navigation(
                markup=markup,
                page_size=page_size,
                page_number=state.page_number,
                number_of_matches=match_repository.count_by_genre(state.item_id)
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
    elif state.progress == VeiwByGenreProgress.VEIW_ONE_FILTERED_BY_GENRE:
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


def veiw_by_loneliness_presentation(state: VeiwByLonelinessState):
    if state.progress == VeiwByLonelinessProgress.CHOOSE_LONELINESS_STATUS:
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
    elif state.progress == VeiwByLonelinessProgress.VEIW_FILTERED_BY_LONELINESS:
        markup = types.InlineKeyboardMarkup()
        page_size = 8
        matches = match_repository.read_by_loneliness(
            loneliness_status=state.status,
            limit=page_size, 
            offset=((state.page_number - 1) * page_size)
        )

        if len(matches) == 0:
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
            return ScreenPresentation(markup, MessageText.NO_MATCHES_FOUND)
        elif len(matches) > 0:
            for match in matches:
                markup.add(
                    create_button(
                        text=ButtonName.small_match_data(match), 
                        callback=match.id
                    )
                )
            markup = add_navigation(
                markup=markup,
                page_size=page_size,
                page_number=state.page_number,
                number_of_matches=match_repository.count_by_loneliness(state.status)
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
    elif state.progress == VeiwByLonelinessProgress.VEIW_ONE_FILTERED_BY_LONELINESS:
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


def update_match_presentation(state: UpdateMatchState):
    if state.progress == UpdateMatchProgress.CHOOSE_GAME:
        markup = types.InlineKeyboardMarkup()
        page_size = 8
        matches = match_repository.read_by_updating(
            limit=page_size, 
            offset=((state.page_number - 1) * page_size)
        )
        for match in matches:
            markup.add(
                create_button(
                    text=ButtonName.small_match_data(match), 
                    callback=match.id
                )
            )
        markup = add_navigation(
            markup=markup,
            page_size=page_size,
            page_number=state.page_number,
            number_of_matches=match_repository.count_all()
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
    elif state.progress == UpdateMatchProgress.CONFIRM_UPDATING:
        match = state.old_match
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
    elif state.progress == UpdateMatchProgress.UPDATE_NAME:
        markup = types.InlineKeyboardMarkup()
        return ScreenPresentation(markup, MessageText.UPDATING_MATCH + '\n' + '\n' + \
            MessageText.match_data(state.new_match) + '\n' + '\n' + \
                MessageText.SET_NAME)
    elif state.progress == UpdateMatchProgress.UPDATE_START_TIME:
        markup = types.InlineKeyboardMarkup()
        return ScreenPresentation(markup, MessageText.UPDATING_MATCH + '\n' + '\n' + \
            MessageText.match_data(state.new_match) + '\n' + '\n' + \
                MessageText.SET_DATETIME)
    elif state.progress == UpdateMatchProgress.UPDATE_START_TIME_AGAIN:
        markup = types.InlineKeyboardMarkup()
        return ScreenPresentation(markup, MessageText.UPDATING_MATCH + '\n' + '\n' + \
            MessageText.match_data(state.new_match) + '\n' + '\n' + \
                MessageText.SET_DATETIME_AGAIN)
    elif state.progress == UpdateMatchProgress.UPDATE_PLACE:
        markup = types.InlineKeyboardMarkup()
        return ScreenPresentation(markup, MessageText.UPDATING_MATCH + '\n' + '\n' + \
            MessageText.match_data(state.new_match) + '\n' + '\n' + \
                MessageText.SET_PLACE)
    elif state.progress == UpdateMatchProgress.UPDATE_GROUP:
        markup = types.InlineKeyboardMarkup()
        groups = group_repository.read_all()
        for group in groups:
            markup.add(
                create_button(
                    text=group.name, 
                    callback=group.id
                )
            )
        return ScreenPresentation(markup, MessageText.UPDATING_MATCH + '\n' + '\n' + \
            MessageText.match_data(state.new_match) + '\n' + '\n' + \
                MessageText.SET_GROUP)
    elif state.progress == UpdateMatchProgress.UPDATE_GENRE:
        markup = types.InlineKeyboardMarkup()
        genres = genre_repository.read_all()
        for genre in genres:
            markup.add(
                create_button(
                    text=genre.name, 
                    callback=genre.id
                )
            )
        return ScreenPresentation(markup, MessageText.UPDATING_MATCH + '\n' + '\n' + \
            MessageText.match_data(state.new_match) + '\n' + '\n' + \
                MessageText.SET_GENRE)
    elif state.progress == UpdateMatchProgress.UPDATE_LONELINESS:
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
        return ScreenPresentation(markup, MessageText.UPDATING_MATCH + '\n' + '\n' + \
            MessageText.match_data(state.new_match) + '\n' + '\n' + \
                MessageText.SET_LONELINESS)
    elif state.progress == UpdateMatchProgress.UPDATE_URL:
        markup = types.InlineKeyboardMarkup()
        return ScreenPresentation(markup, MessageText.UPDATING_MATCH + '\n' + '\n' + \
            MessageText.match_data(state.new_match) + '\n' + '\n' + \
                MessageText.SET_URL)
    elif state.progress == UpdateMatchProgress.COMPARING_EDITIONS:
        markup = types.InlineKeyboardMarkup()
        markup.add(
            create_button(
                text=ButtonName.UPDATE_NAME,
                callback=ButtonCallback.UPDATE_NAME
            )
        )
        markup.add(
            create_button(
                text=ButtonName.UPDATE_START_TIME,
                callback=ButtonCallback.UPDATE_START_TIME
            )
        )
        markup.add(
            create_button(
                text=ButtonName.UPDATE_PLACE,
                callback=ButtonCallback.UPDATE_PLACE
            )
        )
        markup.add(
            create_button(
                text=ButtonName.UPDATE_GROUP,
                callback=ButtonCallback.UPDATE_GROUP
            )
        )
        markup.add(
            create_button(
                text=ButtonName.UPDATE_GENRE,
                callback=ButtonCallback.UPDATE_GENRE
            )
        )
        markup.add(
            create_button(
                text=ButtonName.UPDATE_LONELINESS,
                callback=ButtonCallback.UPDATE_LONELINESS
            )
        )
        markup.add(
            create_button(
                text=ButtonName.UPDATE_URL,
                callback=ButtonCallback.UPDATE_URL
            )
        )
        markup.add(
            create_button(
                text=ButtonName.CANCEL_GAME_EDITING,
                callback=ButtonCallback.CANCEL_GAME_EDITING
            ),
            create_button(
                text=ButtonName.SAVE_GAME,
                callback=ButtonCallback.SAVE_GAME
            )
        )
        return ScreenPresentation(markup, MessageText.CURRENT_MATCH + '\n' + '\n' + \
            MessageText.match_data(state.old_match) + '\n' + '\n' + \
            MessageText.UPDATING_MATCH + '\n' + '\n' + \
            MessageText.match_data(state.new_match) + '\n' + '\n' + \
                MessageText.UPDATING_PROCESS)
    elif state.progress == UpdateMatchProgress.FINISH_UPDATING:
        markup = types.InlineKeyboardMarkup()
        markup.add(
            create_button(
                text=ButtonName.YES,
                callback=ButtonCallback.FINISH_UPDATING
            )
        )
        markup.add(
            create_button(
                text=ButtonName.NO,
                callback=ButtonCallback.CANCEL_UPDATING
            )
        )
        return ScreenPresentation(markup, MessageText.INSURE_UPDATING)
    

def game_is_updated_presentation(state: GameIsUpdatedState):
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
    return ScreenPresentation(markup, MessageText.GAME_UPDATED)


def game_updating_is_cancelled_presentation(state: GameUpdatingIsCancelledState):
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
    return ScreenPresentation(markup, MessageText.GAME_UPDATING_IS_CANCELLED)


def error_presentation(state):
    markup = types.InlineKeyboardMarkup()
    markup.add(
        create_button(
            text=ButtonName.MAIN_MENU, 
            callback=ButtonCallback.MAIN_MENU
        )
    )
    return ScreenPresentation(markup, 'Экран находится в разработке')


def subscribtion_presentation(state: SubscriptionState):
    markup = types.InlineKeyboardMarkup()
    if state.is_subscribed:
        markup.add(
            create_button(
                text=ButtonName.DELETE_SUBSCRIPTION, 
                callback=ButtonCallback.DELETE_SUBSCRIPTION
            )
        )
        markup.add(
            create_button(
                text=ButtonName.MAIN_MENU, 
                callback=ButtonCallback.MAIN_MENU
            ),
            create_button(
                text=ButtonName.GO_BACK, 
                callback=ButtonCallback.SCHEDULE
            )
        )
        return ScreenPresentation(markup, MessageText.SUBSCRIPTION)
    else:
        markup.add(
            create_button(
                text=ButtonName.CREATE_SUBSCRIPTION, 
                callback=ButtonCallback.CREATE_SUBSCRIPTION
            )
        )
        markup.add(
            create_button(
                text=ButtonName.MAIN_MENU, 
                callback=ButtonCallback.MAIN_MENU
            ),
            create_button(
                text=ButtonName.GO_BACK, 
                callback=ButtonCallback.SCHEDULE
            )
        )
        return ScreenPresentation(markup, MessageText.SUBSCRIPTION)

def subscribtion_managed_presentation(state: SubscriptionManagedState):
    markup = types.InlineKeyboardMarkup()
    markup.add(
            create_button(
                text=ButtonName.MAIN_MENU, 
                callback=ButtonCallback.MAIN_MENU
            ),
            create_button(
                text=ButtonName.GO_BACK, 
                callback=ButtonCallback.SUBSCRIBE
            )
        )
    if state.is_created:
        return ScreenPresentation(markup, MessageText.SUBSCRIPTION_CREATED)
    else:
        return ScreenPresentation(markup, MessageText.SUBSCRIPTION_DELETED)