from telebot import types


def create_button(text: str, callback: str) -> types.InlineKeyboardButton:
    return types.InlineKeyboardButton(
        text=text,
        callback_data=callback
    )


def create_multiselect_button(text: str, is_selected: bool, callback: str) -> types.InlineKeyboardButton:
    if is_selected:
        text += ' ✅'
    return types.InlineKeyboardButton(
        text=text,
        callback_data=callback
    )
