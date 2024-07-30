from telebot import types


class Button():
    def __init__(self, name, callback):
        self.name = name
        self.callback = callback
    
    name: str
    callback: str
