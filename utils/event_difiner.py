from states_events.events import *
from states_events.menu_content.button_callbacks import ButtonCallback


def define_button_event(callback_data: str) -> ButtonEvent:
    return {
        ButtonCallback.MAIN_MENU: MainMenuEvent,
        ButtonCallback.HOW_TO: HowToEvent,
        ButtonCallback.MARKET: MarketEvent,
        #will be continued
    }[callback_data]()

def define_message_event(message_text: str) -> MessageEvent:
    pass
