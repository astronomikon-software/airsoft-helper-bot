from menu_operator.state_machine.bot_states import *
from menu_operator.consts.button_callback import ButtonCallback
from utils.state_machine import StateMachine
from menu_operator.state_machine.bot_events import *


def create_bot_state_machine() -> StateMachine:
    state_machine = StateMachine()
    state_machine.register(
        BotState,
        MoveToMainMenuEvent,
        lambda _, __: MainMenuState(),
    )
    state_machine.register(
        BotState, 
        MoveToScheduleEvent, 
        lambda _, __: ScheduleState(),
    )
    state_machine.register(
        BotState, 
        MoveToMarketEvent, 
        lambda _, __: MarketState(),
    )
    state_machine.register(
        BotState, 
        MoveToHowToEvent, 
        lambda _, __: HowToState(),
    )
    state_machine.register(
        BotState, 
        MoveToCalendarEvent, 
        lambda _, __: CalendarState(),
    )
    state_machine.register(
        BotState, 
        MoveToFiltersEvent, 
        lambda _, __: FiltersState(),
    )

    def from_schedule_to_organisers(state: BotState, event: MoveToOrganisersEvent) -> BotState:
        if event.user.is_admin == True:
            if event.user.is_true_admin == True:
                return HighOrganisersState()
            return MiddleOrganisersState()
        else:
            return LowOrganisersState()
    
    state_machine.register(
        BotState,
        MoveToOrganisersEvent,
        from_schedule_to_organisers,
    )
    state_machine.register(
        BotState,
        MoveToSetDatetimeEvent,
        lambda _, __: SetDatetimeState()
    )
    state_machine.register(
        BotState,
        MoveToSetDatetimeEvent,
        lambda _, __: SetDatetimeState()
    )
    return state_machine
