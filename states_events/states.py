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

class CalendarProgress():
    VEIW_ALL = 'VEIW_ALL'
    VEIW_ONE = 'VEIW_ONE'

class CalendarState(BotState):
    progress: CalendarProgress
    match_id: int
    page_number: int

    def __init__(self, match_id, progress, page_number):
        self.match_id = match_id
        self.page_number = page_number
        self.progress = progress


class FiltersState(BotState):
    pass

class VeiwByPlaceProgress():
    VEIW_PLACES = 'VEIW_PLACES'
    VEIW_FILTERED_BY_PLACE = 'VEIW_FILTERED_BY_PLACE'
    VEIW_ONE_FILTERED_BY_PLACE = 'VEIW_ONE_FILTERED_BY_PLACE'

class VeiwByPlaceState(BotState):
    progress: VeiwByPlaceProgress
    item_id: int
    match_id: int
    page_number: int

    def __init__(self, item_id, match_id, progress, page_number):
        self.item_id = item_id
        self.match_id = match_id
        self.progress = progress
        self.page_number = page_number

class VeiwByGroupProgress():
    VEIW_GROUPS = 'VEIW_GROUPS'
    VEIW_FILTERED_BY_GROUP = 'VEIW_FILTERED_BY_GROUP'
    VEIW_ONE_FILTERED_BY_GROUP = 'VEIW_ONE_FILTERED_BY_GROUP'

class VeiwByGroupState(BotState):
    progress: VeiwByGroupProgress
    item_id: int
    match_id: int
    page_number: int

    def __init__(self, item_id, match_id, progress, page_number):
        self.item_id = item_id
        self.match_id = match_id
        self.progress = progress
        self.page_number = page_number

class VeiwByGenreProgress():
    VEIW_GENRES = 'VEIW_GENRES'
    VEIW_FILTERED_BY_GENRE = 'VEIW_FILTERED_BY_GENRE'
    VEIW_ONE_FILTERED_BY_GENRE = 'VEIW_ONE_FILTERED_BY_GENRE'

class VeiwByGenreState(BotState):
    progress: VeiwByGenreProgress
    item_id: int
    match_id: int
    page_number: int

    def __init__(self, item_id, match_id, progress, page_number):
        self.item_id = item_id
        self.match_id = match_id
        self.progress = progress
        self.page_number = page_number

class VeiwByLonelinessProgress():
    CHOOSE_LONELINESS_STATUS = 'CHOOSE_LONELINESS_STATUS'
    VEIW_FILTERED_BY_LONELINESS = 'VEIW_FILTERED_BY_LONELINESS'
    VEIW_ONE_FILTERED_BY_LONELINESS = 'VEIW_ONE_FILTERED_BY_LONELINESS'

class VeiwByLonelinessState(BotState):
    progress: VeiwByLonelinessProgress
    match_id: int
    status: str
    page_number: int

    def __init__(self, status: str, match_id, progress, page_number):
        self.status = status
        self.match_id = match_id
        self.progress = progress
        self.page_number = page_number

# organisers branches

class OrganisersState(BotState):
    pass

# new game

class EditMatchProgress():
    START_TIME = 'START_TIME'
    START_TIME_AGAIN = 'START_TIME_AGAIN'
    DURATION = 'DURATION'
    PLACE = 'PLACE'
    GROUP ='GROUP'
    GENRE = 'GENRE'
    IS_LONELINESS_FRIENDLY = 'IS_LONELINESS_FRIENDLY'
    CONFIRMATION ='CONFIRMATION'

class EditMatchState(BotState):
    match: Match
    progress: EditMatchProgress

    def __init__(
        self,
        match: Match,
        progress: EditMatchProgress,
    ):
        self.match = match
        self.progress = progress

class GameIsSavedState(BotState):
    pass

class GameIsCancelledState(BotState):
    pass
    
# edit game

class UpdateMatchProgress():
    CHOOSE_GAME = 'CHOOSE_GAME'
    CONFIRM_UPDATING = 'CONFIRM_UPDATING'
    UPDATE_START_TIME = 'UPDATE_START_TIME'
    UPDATE_START_TIME_AGAIN = 'UPDATE_START_TIME_AGAIN'
    UPDATE_PLACE = 'UPDATE_PLACE'
    UPDATE_GROUP = 'UPDATE_GROUP'
    UPDATE_GENRE = 'UPDATE_GENRE'
    UPDATE_LONELINESS = 'UPDATE_LONELINESS'
    COMPARING_EDITIONS = 'COMPARING_EDITIONS'
    FINISH_UPDATING = 'FINISH_UPDATING'

# class UpdateMatchState(BotState):
#     match_id: int
#     progress: UpdateMatchProgress
#     page_number: int

#     def __init__(
#         self,
#         match_id: int,
#         progress: UpdateMatchProgress,
#         page_number: int
#     ):
#         self.match_id = match_id
#         self.progress = progress
#         self.page_number = page_number

class UpdateMatchState(BotState):
    old_match: Match
    new_match: Match
    progress: UpdateMatchProgress
    page_number: int

    def __init__(
        self,
        old_match: Match,
        new_match: Match,
        progress: UpdateMatchProgress,
        page_number: int
    ):
        self.old_match = old_match
        self.new_match = new_match
        self.progress = progress
        self.page_number = page_number

class GameIsUpdatedState(BotState):
    pass

class GameUpdatingIsCancelledState(BotState):
    pass
