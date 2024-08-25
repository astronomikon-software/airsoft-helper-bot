import json #to think about
from model.user import User
from states_events.states import StartState


def get_default_user(user_id: int) -> User:
    user = User()
    user.id = user_id
    user.state_id = json.dumps({'state_name': StartState.__name__}) #to think about
    user.is_admin = False
    user.is_true_admin = False
    return user