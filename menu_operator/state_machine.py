from typing import Type
from abc import ABC



class State(ABC):
    pass
class Event(ABC):
    pass

class StateMachine:   
    def __init__(self):
        self.handlers = {}

    def register(self, state_class: Type, event_class: Type, handler):
        self.handlers.update({event_class: {state_class: handler}})

    def handle(self, old_state: State, event: Event):
        if type(event) in self.handlers:
            if type(old_state) in self.handlers[type(event)]:
                return self.handlers[type(event)][type(old_state)](old_state, event)
            

'''
def market_button_handler(old_state: State, event: Event) -> State:
    market_state = MarketState()
    market_state.disclaimer = 'haha hihi'
    return market_state

state_machine = StateMachine()
main_menu_state = MainMenuState()
button_event = ButtonEvent()

state_machine.register(MainMenuState, ButtonEvent, market_button_handler)
new_state = state_machine.handle(main_menu_state, button_event)
print(new_state.disclaimer)
'''