from telebot import types


class Button():
    def __init__(self, name, callback):
        self.name = name
        self.callback = callback
    
    name: str
    callback: str

def create_button(button: Button):
    button = types.InlineKeyboardButton(button.name, callback_data=button.callback)
    return button

def create_markup():
    markup = types.InlineKeyboardMarkup()
    return markup
