from abc import ABC


class BotEvent(ABC):
    pass

#or to do two other subclasses in the middle of this scheme:
#
#class ButtonEvent(BotEvent):
#    pass
#
#class MessageEvent(BotEvent):
#    pass

class MainMenuEvent(BotEvent):
    pass

class MarketEvent(BotEvent):
    pass

class HowToEvent(BotEvent):
    pass

class ScheduleEvent(BotEvent):
    pass

class CalendarEvent(BotEvent):
    pass

class FiltersEvent(BotEvent):
    pass

class OrganisersEvent(BotEvent):
    pass

class SetDatetimeEvent(BotEvent):
    pass

class SetPlaceEvent(BotEvent):
    pass

class SetGroupEvent(BotEvent):
    pass

class SetGenreEvent(BotEvent):
    pass

class SetLonelinessEvent(BotEvent):
    pass