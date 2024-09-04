from telebot import types


def create_button(text, callback) -> types.InlineKeyboardButton:
    return types.InlineKeyboardButton(
        text=text,
        callback_data=callback
    )
