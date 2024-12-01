from telebot import types
from datetime import datetime
from dateutil.relativedelta import relativedelta
import calendar

from mapping.datetime_mapping import str_time_to_int
from utils.button_util import create_button
from states_events.menu_content.button_callbacks import ButtonCallback


def shift_date(date, months):
    return date + relativedelta(months=months)


def add_calendar(markup: types.InlineKeyboardMarkup, day: datetime) -> types.InlineKeyboardMarkup:
    month = day.month
    year = day.year

    cal = calendar.Calendar(firstweekday=calendar.MONDAY)
    days = cal.monthdayscalendar(year, month)

    month_name = { # or just calendar.month_name[month] for god forsaken English language
        1: 'Январь',
        2: 'Февраль',
        3: 'Март',
        4: 'Апрель',
        5: 'Май',
        6: 'Июнь',
        7: 'Июль',
        8: 'Август',
        9: 'Сентябрь',
        10: 'Октябрь',
        11: 'Ноябрь',
        12: 'Декабрь',
    }[month]
    markup.add(types.InlineKeyboardButton(f"{month_name} {year}", callback_data='ignore'))

    weekdays = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
    markup.add(*[create_button(text=str(day), callback=ButtonCallback.VOID) for day in weekdays])

    for week in days:
        row_buttons = []
        for day in week:
            if day == 0:
                row_buttons.append(create_button(' ', callback=ButtonCallback.VOID))
            else:
                row_buttons.append(create_button(text=str(day), callback=str(str_time_to_int(f'{day}.{month}.{year}'))))
        markup.add(*row_buttons)

    return markup