import telebot
from telebot import types
from menu_buttons.button_callback import ButtonCallback


to_main_menu_button = types.InlineKeyboardButton('Вернуться к главному меню', callback_data=ButtonCallback.TO_MAIN_MENU)

class MainMenuButtons:
    button1 = types.InlineKeyboardButton('Расписание игр', callback_data=ButtonCallback.SCHEDULE)
    button2 = types.InlineKeyboardButton('Как начать играть в страйкбол', url='https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    button3 = types.InlineKeyboardButton('Барахолка', callback_data=ButtonCallback.MARKET)

class ScheduleButtons:
    button1 = types.InlineKeyboardButton('Просмотр календаря', callback_data=ButtonCallback.CALENDAR)
    button2 = types.InlineKeyboardButton('Просмотр по фильтрам', callback_data=ButtonCallback.FILTERS)
    button3 = types.InlineKeyboardButton('Организаторам', callback_data=ButtonCallback.TO_ORGANISERS)
    go_back_button = types.InlineKeyboardButton('◀️', callback_data=ButtonCallback.TO_MAIN_MENU)

class FilterButtons:
    button1 = types.InlineKeyboardButton('Просмотр по жанрам', callback_data=ButtonCallback.GENRES)
    button2 = types.InlineKeyboardButton('Просмотр по полигонам', callback_data=ButtonCallback.PLACES)
    button3 = types.InlineKeyboardButton('Просмотр по орг.группам', callback_data=ButtonCallback.GROUPS)
    button4 = types.InlineKeyboardButton('Подходит ли для одиночек', callback_data=ButtonCallback.LONELINESS)
    go_back_button = types.InlineKeyboardButton('◀️', callback_data=ButtonCallback.SCHEDULE)

