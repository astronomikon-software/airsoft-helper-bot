from telebot import types


def create_button(button_name: str, button_callback=None):
    button = types.InlineKeyboardButton(button_name, callback_data=button_callback)
    return button
