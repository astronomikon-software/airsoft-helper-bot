from abc import ABC
from button_name import ButtonName
from button_callback import ButtonCallback
from message_text import MessageText
from create_button import Button

class State(ABC):
    pass
class Event(ABC):
    pass

class MessageEvent(Event):
    message: object
class ButtonEvent(Event):
    callback: object

class StartState(State):
    pass
class MainMenuState(State):
    buttons = [
        Button(ButtonName.SCHEDULE, ButtonCallback.SCHEDULE), 
        Button(ButtonName.HOW_TO, ButtonCallback.HOW_TO), 
        Button(ButtonName.MARKET, ButtonCallback.MARKET)
        ]
    message_text = MessageText.HELLO
class MarketState(State):
    buttons = [
        Button(ButtonName.MAIN_MENU, ButtonCallback.MAIN_MENU)
        ]
    message_text = MessageText.MARKET
class HowToState(State):
    buttons = [
        Button(ButtonName.MAIN_MENU, ButtonCallback.MAIN_MENU)
        ]
    message_text = MessageText.HOW_TO
class ScheduleState(State):
    message_text = MessageText.HOW_TO
class CalendarState(State):
    pass
class FiltersState(State):
    pass
