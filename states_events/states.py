from abc import ABC
from enum import Enum

from model.match import Match


class BotState():
    pass

class StartState(BotState):
    pass

# main_menu branch

class MainMenuState(BotState):
    pass

class MarketState(BotState):
    pass

class HowToState(BotState):
    pass

#schedule branch

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

class VeiwByPlaceState(BotState):
    class Progress(Enum):
        VEIW_PLACES = 'VEIW_PLACES'
        VEIW_FILTERED_BY_PLACE = 'VEIW_FILTERED_BY_PLACE'
        VEIW_ONE_FILTERED_BY_PLACE = 'VEIW_ONE_FILTERED_BY_PLACE'
    
    progress: Progress
    item_id: int
    match_id: int

    def __init__(self, item_id, match_id, progress):
        self.item_id = item_id
        self.match_id = match_id
        self.progress = progress

class VeiwByGroupState(BotState):
    class Progress(Enum):
        VEIW_GROUPS = 'VEIW_GROUPS'
        VEIW_FILTERED_BY_GROUP = 'VEIW_FILTERED_BY_GROUP'
        VEIW_ONE_FILTERED_BY_GROUP = 'VEIW_ONE_FILTERED_BY_GROUP'
    
    progress: Progress
    item_id: int
    match_id: int

    def __init__(self, item_id, match_id, progress):
        self.item_id = item_id
        self.match_id = match_id
        self.progress = progress

class VeiwByGenreState(BotState):
    class Progress(Enum):
        VEIW_GENRES = 'VEIW_GENRES'
        VEIW_FILTERED_BY_GENRE = 'VEIW_FILTERED_BY_GENRE'
        VEIW_ONE_FILTERED_BY_GENRE = 'VEIW_ONE_FILTERED_BY_GENRE'
    
    progress: Progress
    item_id: int
    match_id: int

    def __init__(self, item_id, match_id, progress):
        self.item_id = item_id
        self.match_id = match_id
        self.progress = progress

class VeiwByLonelinessState(BotState):
    class Progress(Enum):
        CHOOSE_LONELINESS_STATUS = 'CHOOSE_LONELINESS_STATUS'
        VEIW_FILTERED_BY_LONELINESS = 'VEIW_FILTERED_BY_LONELINESS'
        VEIW_ONE_FILTERED_BY_LONELINESS = 'VEIW_ONE_FILTERED_BY_LONELINESS'
    
    progress: Progress
    match_id: int
    status: str

    def __init__(self, status: str, match_id, progress):
        self.status = status
        self.match_id = match_id
        self.progress = progress

# organisers branches

class OrganisersState(BotState):
    pass

# new game

class SetNewMatchState(BotState):
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
    
# edit game
