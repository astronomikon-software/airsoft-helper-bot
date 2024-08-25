import json
from states_events.states import *


def str_to_class_object(classname):
    return globals()[classname]()


def state_to_json_str(state: BotState) -> dict:
    if isinstance(state, SetDatetimeState):
        pass
    
    #elif <other exceptions>
    
    else:
        return json.dumps({'state_name': type(state).__name__})


def json_str_to_state(json_str_state) -> BotState:
    dict_state = json.loads(json_str_state)
    
    if dict_state['state_name'] == SetDatetimeState.__name__:
        pass
    
    #elif <other exceptions>

    else:
        return str_to_class_object(dict_state['state_name'])

