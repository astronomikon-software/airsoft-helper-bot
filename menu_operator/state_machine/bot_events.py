from utils.state_machine import Event


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
