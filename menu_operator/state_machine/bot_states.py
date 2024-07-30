from menu_operator.consts.button_name import ButtonName
from menu_operator.consts.button_callback import ButtonCallback
from menu_operator.consts.message_text import MessageText
from menu_operator.bot_button import Button
from utils.state_machine import State, Event


class BotState(State):
    buttons: list[Button] = []
    message_text: str


class StartState(BotState):
    pass

class MainMenuState(BotState):
    buttons = [
        Button(ButtonName.SCHEDULE, ButtonCallback.SCHEDULE), 
        Button(ButtonName.HOW_TO, ButtonCallback.HOW_TO), 
        Button(ButtonName.MARKET, ButtonCallback.MARKET)
    ]
    message_text = MessageText.HELLO

class MarketState(BotState):
    buttons = [
        Button(ButtonName.MAIN_MENU, ButtonCallback.MAIN_MENU)
    ]
    message_text = MessageText.MARKET

class HowToState(BotState):
    buttons = [
        Button(ButtonName.MAIN_MENU, ButtonCallback.MAIN_MENU)
    ]
    message_text = MessageText.HOW_TO

class ScheduleState(BotState):
    message_text = MessageText.CHOOSE_FUNCTION

class CalendarState(BotState):
    message_text = MessageText.CHOOSE_FUNCTION

class FiltersState(BotState):
    message_text = MessageText.CHOOSE_FUNCTION
