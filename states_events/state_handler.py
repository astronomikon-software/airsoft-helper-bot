from states_events.states import *
from telebot import types

from states_events.menu_content.button_names import ButtonName
from states_events.menu_content.button_callbacks import ButtonCallback
from states_events.menu_content.message_texts import MessageText


class ScreenPresentation:
    def __init__(self, markup, message_text):
        self.markup = markup
        self.message_text = message_text

    markup: types.InlineKeyboardMarkup
    message_text: str


def handle_state(state: BotState):
    if isinstance(state, MainMenuState) == True:
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(ButtonName.SCHEDULE, ButtonCallback.SCHEDULE))
        markup.add(types.InlineKeyboardButton(ButtonName.HOW_TO, ButtonCallback.HOW_TO))
        markup.add(types.InlineKeyboardButton(ButtonName.MARKET, ButtonCallback.MARKET))
        return ScreenPresentation(markup, MessageText.HELLO)
    
    elif isinstance(state, HowToState) == True:
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(ButtonName.MAIN_MENU, ButtonCallback.MAIN_MENU))
        return ScreenPresentation(markup, MessageText.HOW_TO)
    
    elif isinstance(state, MarketState) == True:
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(ButtonName.MAIN_MENU, ButtonCallback.MAIN_MENU))
        return ScreenPresentation(markup, MessageText.MARKET)

