from abc import ABC


class BotState(ABC):
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

class SetDatetimeState(BotState):
    pass
    #some data

class SetPlaceState(BotState):
    pass

class SetGroupState(BotState):
    pass

class SetGenreState(BotState):
    pass

class SetLonelinessState(BotState):
    pass