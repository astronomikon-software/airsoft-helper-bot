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
    class Progress(Enum):
        VEIW_ALL = 'VEIW_ALL'
        VEIW_ONE = 'VEIW_ONE'
    
    progress: Progress
    match_id: int

    def __init__(self, match_id, progress):
        self.match_id = match_id
        self.progress = progress

class FiltersState(BotState):
    pass

class OrganisersState(BotState):
    pass

class EditMatchState(BotState):
    class Progress(Enum):
        START_TIME = 'START_TIME'
        START_TIME_AGAIN = 'START_TIME_AGAIN'
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
    

