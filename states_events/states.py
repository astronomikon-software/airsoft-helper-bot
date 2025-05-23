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

class HelpState(BotState):
    pass

class DonateState(BotState):
    pass

#schedule branch

class ScheduleState(BotState):
    pass

class CalendarProgress():
    VEIW_ALL = 'VEIW_ALL'
    VEIW_ONE = 'VEIW_ONE'

class CalendarState(BotState):
    progress: CalendarProgress
    match_id: int | None
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
    place_name: int
    match_id: int
    page_number: int

    def __init__(self, item_id, match_id, progress, page_number):
        self.place_name = item_id
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
    status: bool
    page_number: int

    def __init__(self, status: bool, match_id, progress, page_number):
        self.status = status
        self.match_id = match_id
        self.progress = progress
        self.page_number = page_number

class VeiwByDurationProgress():
    VEIW_DURATIONS = 'VEIW_DURATIONS'
    VEIW_FILTERED_BY_DURATION = 'VEIW_FILTERED_BY_DURATION'
    VEIW_ONE_FILTERED_BY_DURATION = 'VEIW_ONE_FILTERED_BY_DURATION'

class VeiwByDurationState(BotState):
    progress: VeiwByPlaceProgress
    item_id: int
    match_id: int
    page_number: int

    def __init__(self, item_id, match_id, progress, page_number):
        self.item_id = item_id
        self.match_id = match_id
        self.progress = progress
        self.page_number = page_number

class VeiwByDateProgress():
    VEIW_DATES = 'VEIW_DATES'
    VEIW_FILTERED_BY_DATE = 'VEIW_FILTERED_BY_DATE'
    VEIW_ONE_FILTERED_BY_DATE = 'VEIW_ONE_FILTERED_BY_DATE'

class VeiwByDateState(BotState):
    progress: VeiwByDateProgress
    month_offset: int
    date: int
    match_id: int

    def __init__(self, progress: VeiwByDateProgress, month_offset: int, date: int, match_id: int):
        self.progress = progress
        self.month_offset = month_offset
        self.date = date
        self.match_id = match_id

# subscription branch

class SubscriptionState(BotState):
    is_subscribed: bool

    def __init__(self, is_subscribed: bool):
        self.is_subscribed = is_subscribed

class SubscriptionManagedState(BotState):
    is_created: bool

    def __init__(self, is_created: bool):
        self.is_created = is_created

# organisers branches

class OrganisersState(BotState):
    pass

# new game

class EditMatchProgress():
    NAME = 'NAME'
    START_TIME = 'START_TIME'
    START_TIME_AGAIN = 'START_TIME_AGAIN'
    DURATION = 'DURATION'
    PLACE = 'PLACE'
    GROUP ='GROUP'
    GENRE = 'GENRE'
    IS_LONELINESS_FRIENDLY = 'IS_LONELINESS_FRIENDLY'
    URL = 'URL'
    ANNOTATION = 'ANNOTATION'
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
    UPDATE_NAME = 'UPDATE_NAME'
    UPDATE_START_TIME = 'UPDATE_START_TIME'
    UPDATE_START_TIME_AGAIN = 'UPDATE_START_TIME_AGAIN'
    UPDATE_DURATION = 'UPDATE_DURATION'
    UPDATE_PLACE = 'UPDATE_PLACE'
    UPDATE_GROUP = 'UPDATE_GROUP'
    UPDATE_GENRE = 'UPDATE_GENRE'
    UPDATE_LONELINESS = 'UPDATE_LONELINESS'
    UPDATE_URL = 'UPDATE_URL'
    UPDATE_ANNOTATION = 'UPDATE_ANNOTATION'
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
