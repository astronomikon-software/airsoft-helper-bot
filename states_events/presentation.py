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

    elif isinstance(state, AfterConfirmationState):
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

    else:
        markup = types.InlineKeyboardMarkup()
        markup.add(
            create_button(
                text=ButtonName.MAIN_MENU, 
                callback=ButtonCallback.MAIN_MENU
            )
        )
        return ScreenPresentation(markup, 'Представление не определено')
