from menu_operator.state_machine.bot_states import State, Event
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
    return state_machine
