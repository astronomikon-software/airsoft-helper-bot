from utils.state_machine import Event
from model.user import User
from model.match import Match


class BotEvent(Event):
    pass

class MoveToMainMenuEvent(BotEvent):
    pass

class MoveToScheduleEvent(BotEvent):
    pass

class MoveToMarketEvent(BotEvent):
    pass

class MoveToHowToEvent(BotEvent):
    pass

class MoveToCalendarEvent(BotEvent):
    pass

class MoveToFiltersEvent(BotEvent):
    pass

class MoveToOrganisersEvent(BotEvent):
    def __init__(self, user: User):
        self.user = user
    user: User

class MoveToSetDatetimeEvent(BotEvent):
    def __init__(self):
        self.match = Match()
    match: Match

class MoveToChoosePlaceEvent(BotEvent):
    def __init__(self, match):
        self.match = match
    match: Match

class MoveToChooseGroupEvent(BotEvent):
    def __init__(self, match):
        self.match = match
    match: Match

class MoveToChooseGenreEvent(BotEvent):
    def __init__(self, match):
        self.match = match
    match: Match

class MoveToConfirmNewGameEvent(BotEvent):
    def __init__(self, match):
        self.match = match
    match: Match
