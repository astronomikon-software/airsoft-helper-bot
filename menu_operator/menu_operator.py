import telebot
from telebot import types
from configuration import BOT_TOKEN, PSQL_DATABASE, PSQL_USER, PSQL_PASSWORD

from menu_buttons.message_text import MessageText
from menu_buttons.create_button import create_button
from menu_buttons.button_name import ButtonName
from menu_buttons.button_callback import ButtonCallback

from model.user import User
from model.match import Match
from model.genre import Genre
from model.group import Group
from model.place import Place

from data.db_provider import DbProvider
from repository.user_repository import UserRepository
from repository.match_repository import MatchRepository
from repository.genre_repository import GenreRepository
from repository.group_repository import GroupRepository
from repository.place_repository import PlaceRepository


class MenuOperator:
    def __init__(self, previous_state, event_happened) -> None:
        self.old_state = previous_state
        self.event = event_happened

    def operate(self):
        if self.old_state.state_id == ButtonCallback.TO_MAIN_MENU:
            self.to_main_menu()
        elif self.id == ButtonCallback.SCHEDULE:
            self.schedule()

    def to_main_menu(self):
        if self.event.message:
            if self.event.data == ButtonCallback.TO_MAIN_MENU:
                markup = types.InlineKeyboardMarkup()
                markup.add(create_button(ButtonName.SCHEDULE, ButtonCallback.SCHEDULE))
                markup.add(create_button(ButtonName.HOW_TO, ButtonCallback.HOW_TO))
                markup.add(create_button(ButtonName.MARKET, ButtonCallback.MARKET))
                bot.edit_message_text(chat_id=self.event.message.chat.id, message_id=self.event.message.message_id, text=MessageText.HELLO)
                bot.edit_message_reply_markup(chat_id=self.event.message.chat.id, message_id=self.event.message.message_id, reply_markup=markup)
