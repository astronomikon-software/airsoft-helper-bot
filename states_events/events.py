from abc import ABC


class BotEvent(ABC):
    pass

class ButtonEvent(BotEvent):
    callback: str
    
    def __init__(self, callback: str):
        self.callback = callback

class MessageEvent(BotEvent):
    text: str

    def __init__(self, text: str):
        self.text = text
