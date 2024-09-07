from abc import ABC
from enum import Enum

from model.match import Match


class BotState():
    pass

class StartState(BotState):
    pass

class MainMenuState(BotState):
    pass

class MarketState(BotState):
    pass

class HowToState(BotState):
    pass

class ScheduleState(BotState):
    pass

class CalendarState(BotState):
    pass

class FiltersState(BotState):
    pass

class OrganisersState(BotState):
    pass

class EditMatchState(BotState):
    class Progress(Enum):
        START_TIME = 'START_TIME'
        DURATION = 'DURATION'
        PLACE = 'PLACE'
        GROUP ='GROUP'
        GENRE = 'GENRE'
        IS_LONELINESS_FRIENDLY = 'IS_LONELINESS_FRIENDLY'
        CONFIRMATION ='CONFIRMATION'
    
    match: Match
    progress: Progress

    def __init__(
        self,
        match: Match,
        progress: Progress,
    ):
        self.match = match
        self.progress = progress

class GameIsSavedState(BotState):
    pass

class GameIsCancelledState(BotState):
    pass
