#does it even have a purpose?

import json
from states_events.states import *
from states_events.events import *
from mapping.state_mapping import *
from repository.user_repository import UserRepository



def save(self, state: BotState, user_id: int):
    if isinstance(state, SetDatetimeEvent):
        pass

    else:
        pass

def load(self, user_id) -> BotState:
    pass
