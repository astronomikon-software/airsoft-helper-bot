from abc import ABC


class BotEvent(ABC):
    pass

class ButtonEvent(BotEvent):
    pass

class MessageEvent(BotEvent):
    pass

class MainMenuEvent(ButtonEvent):
    pass

class MarketEvent(ButtonEvent):
    pass

class HowToEvent(ButtonEvent):
    pass

class ScheduleEvent(ButtonEvent):
    pass

class CalendarEvent(ButtonEvent):
    pass

class FiltersEvent(ButtonEvent):
    pass

class OrganisersEvent(ButtonEvent):
    pass

class SetDatetimeEvent(ButtonEvent):
    pass

#work in progress
class SetPlaceEvent(BotEvent):
    pass

class SetGroupEvent(BotEvent):
    pass

class SetGenreEvent(BotEvent):
    pass

class SetLonelinessEvent(BotEvent):
    pass