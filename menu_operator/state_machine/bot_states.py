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

class ErrorState(BotState):
    message_text = 'Функция на стадии разработки'

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
    buttons = [
        Button(ButtonName.CALENDAR, ButtonCallback.CALENDAR),
        Button(ButtonName.FILTERS, ButtonCallback.FILTERS),
        Button(ButtonName.ORGANISERS, ButtonCallback.ORGANISERS),
        Button(ButtonName.MAIN_MENU, ButtonCallback.MAIN_MENU),
    ]
    message_text = MessageText.CHOOSE_FUNCTION

class CalendarState(BotState):
    buttons = [
        Button(ButtonName.GO_BACK, ButtonCallback.SCHEDULE),
        Button(ButtonName.MAIN_MENU, ButtonCallback.MAIN_MENU)
    ]
    message_text = MessageText.CALENDAR

class FiltersState(BotState):
    buttons = [
        Button(ButtonName.PLACES, ButtonCallback.PLACES),
        Button(ButtonName.GROUPS, ButtonCallback.GROUPS),
        Button(ButtonName.GENRES, ButtonCallback.GENRES),
        Button(ButtonName.GO_BACK, ButtonCallback.SCHEDULE),
        Button(ButtonName.MAIN_MENU, ButtonCallback.MAIN_MENU),
    ]
    message_text = MessageText.FILTERS

class LowOrganisersState(BotState):
    buttons = [
        Button(ButtonName.GO_BACK, ButtonCallback.SCHEDULE),
        Button(ButtonName.MAIN_MENU, ButtonCallback.MAIN_MENU),
    ]
    message_text = MessageText.ORGANISER_APPLICATION

class MiddleOrganisersState(BotState):
    buttons = [
        Button(ButtonName.NEW_GAME, ButtonCallback.CHOOSE_PLACE),
        Button(ButtonName.NEW_GAME, ButtonCallback.CHOOSE_GAME_TO_UPDATE),
        Button(ButtonName.GO_BACK, ButtonCallback.SCHEDULE),
        Button(ButtonName.MAIN_MENU, ButtonCallback.MAIN_MENU),
    ]
    message_text = MessageText.CHOOSE_FUNCTION

class HighOrganisersState(BotState):
    buttons = [
        Button(ButtonName.NEW_GAME, ButtonCallback.SET_DATETIME),
        Button(ButtonName.UPDATE_GAME, ButtonCallback.CHOOSE_GAME_TO_UPDATE),
        Button(ButtonName.SET_ADMIN, ButtonCallback.CHOOSE_GAME_TO_UPDATE),
        Button(ButtonName.GO_BACK, ButtonCallback.SCHEDULE),
        Button(ButtonName.MAIN_MENU, ButtonCallback.MAIN_MENU),
    ]
    message_text = MessageText.CHOOSE_FUNCTION

class SetDatetimeState(BotState):
    message_text = MessageText.SET_DATETIME
