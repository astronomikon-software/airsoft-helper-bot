from menu_operator.state_machine_classes import State, Event
import menu_operator.state_machine_classes as sm_class
from button_callback import ButtonCallback


def from_start(old_state: State, event: Event) -> State:
    new_state = sm_class.MainMenuState
    return new_state

def from_main_menu(old_state: State, event: Event) -> State:
    if event.callback.data == ButtonCallback.MARKET:        
        new_state = sm_class.MarketState
        return new_state

    elif event.callback.data == ButtonCallback.SCHEDULE:
        new_state = sm_class.ScheduleState
        return new_state
    
    elif event.callback.data == ButtonCallback.HOW_TO:
        new_state = sm_class.HowToState
        return new_state