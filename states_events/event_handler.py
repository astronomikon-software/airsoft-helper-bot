from states_events.states import *
from states_events.events import *


def handle_event(state: BotState, event: BotEvent) -> BotState:
    if isinstance(event, MainMenuEvent) == True:
        return MainMenuState()
    
    elif isinstance(event, MarketEvent) == True:
        return MarketState()
    
    elif isinstance(event, HowToEvent) == True:
        return HowToState()
    
    elif isinstance(event, ScheduleEvent) == True:
        return ScheduleState()
    
    elif isinstance(event, CalendarEvent) == True:
        return CalendarState()
