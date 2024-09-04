from states_events.states import MainMenuState
from states_events.states import MainMenuState
from state_repository_fixture import state_repository_fixture



try:
    old_state = MainMenuState()
    rep = state_repository_fixture()
    rep.create(old_state, 123321)
    new_state = rep.read(123321)
    if isinstance(new_state, old_state.__class__):
            print('Всё ок')
except Exception as E:
        print(E)
