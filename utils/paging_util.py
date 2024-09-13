from telebot import types
from utils.button_util import create_button
from states_events.menu_content.button_names import ButtonName
from states_events.menu_content.button_callbacks import ButtonCallback


def add_navigation(markup: types.InlineKeyboardMarkup, page_size: int, page_number: int, number_of_matches: int):
    if page_number == 1 and number_of_matches > page_size: # first page
        return markup.add(
            create_button(
                text=str(page_number), 
                callback=ButtonCallback.VOID
            ),
            create_button(
                text=ButtonName.NEXT_PAGE,
                callback=ButtonCallback.NEXT_PAGE
            )
        )
    elif page_number > 1 and page_number < (number_of_matches + page_size - 1) // page_size: # page in middle
        return markup.add(
            create_button(
                text=ButtonName.PREVIOUS_PAGE, 
                callback=ButtonCallback.PREVIOUS_PAGE
            ),
            create_button(
                text=str(page_number), 
                callback=ButtonCallback.VOID
            ),
            create_button(
                text=ButtonName.NEXT_PAGE, 
                callback=ButtonCallback.NEXT_PAGE
            )
        )
    elif page_number > 1 and page_number == (number_of_matches + page_size - 1) // page_size: # last page !!!
        return markup.add(
            create_button(
                text=ButtonName.PREVIOUS_PAGE,
                callback=ButtonCallback.PREVIOUS_PAGE
            ),
            create_button(
                text=str(page_number), 
                callback=ButtonCallback.VOID
            )
        )
    elif number_of_matches <= page_size: # the only page 
        pass