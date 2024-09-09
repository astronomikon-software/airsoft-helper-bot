from telebot import types


def create_button(text: str, callback: str) -> types.InlineKeyboardButton:
    return types.InlineKeyboardButton(
        text=text,
        callback_data=callback
    )
