import time

import telebot
from telebot import types
from configuration import BOT_TOKEN, PSQL_DATABASE, PSQL_USER, PSQL_PASSWORD

from utils.state_machine import StateMachine
from menu_operator.state_machine.bot_states import *
from menu_operator.state_machine.bot_events import *
from menu_operator.state_machine.bot_state_machine import create_bot_state_machine

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

from utils.datetime_util import str_to_int


bot = telebot.TeleBot(BOT_TOKEN)

db_provider = DbProvider(
    database=PSQL_DATABASE,
    user=PSQL_USER,
    password=PSQL_PASSWORD
)
user_repository = UserRepository(db_provider)
match_repository = MatchRepository(db_provider)
genre_repository = GenreRepository(db_provider)
group_repository = GroupRepository(db_provider)
place_repository = PlaceRepository(db_provider)

genres = genre_repository.read_all()
groups = group_repository.read_all()
places = place_repository.read_all()

'''
def handle_bot_event(event: BotEvent, user_id: int, chat_id: int, message_id=None):
    state_machine = create_bot_state_machine()
    global state
    if isinstance(state, StartState):
        state = state_machine.handle(state, event)
        create_message(state, chat_id)
        user = user_repository.read_or_create(get_default_user(user_id))
    #temporary mera
    else:
        state = state_machine.handle(state, event)
        edit_message(state, chat_id, message_id)
'''

def create_button(button: Button):
    button = types.InlineKeyboardButton(button.name, callback_data=button.callback)
    return button

def create_markup(state: BotState):
    markup = types.InlineKeyboardMarkup()
    for button in state.buttons:
        markup.add(create_button(button))
    return markup

def edit_message(state: BotState, chat_id, message_id):
    markup = create_markup(state)
    bot.edit_message_text(
        chat_id=chat_id,
        message_id=message_id,
        text=state.message_text,
    )
    bot.edit_message_reply_markup(
        chat_id=chat_id,  #callback.message.chat.id,
        message_id=message_id, #callback.message.message_id,
        reply_markup=markup,
    )


def create_message(state: BotState, chat_id):
    markup = create_markup(state)
    bot.send_message(
        chat_id, 
        text=state.message_text, 
        reply_markup=markup,
    )

def get_default_user(user_id: int) -> User:
    user = User()
    user.id = user_id
    user.state_id = StartState.__name__
    user.is_admin = False
    user.is_true_admin = False
    return user

def str_to_class_object(classname):
    return globals()[classname]()


@bot.message_handler(commands=['start'])
def start(message): 
    try:
        state_machine = create_bot_state_machine()
        user = user_repository.read_or_create(get_default_user(message.from_user.id))
        state = state_machine.handle(StartState(), MoveToMainMenuEvent())
        user.state_id = type(state).__name__
        user_repository.update(user)
        create_message(state, message.chat.id)
    except Exception as e:
        print(e)
    '''
    handle_bot_event(
        MoveToMainMenuEvent(),
        message.from_user.id,
        message.chat.id,
    )
    '''


@bot.callback_query_handler(func=lambda callback: True)
def callback_operator(callback):
    '''
    handle_bot_event(
        {
            ButtonCallback.MAIN_MENU: MoveToMainMenuEvent,
            ButtonCallback.SCHEDULE: MoveToScheduleEvent,
            ButtonCallback.MARKET: MoveToMarketEvent,
            ButtonCallback.HOW_TO: MoveToHowToEvent,
            ButtonCallback.FILTERS: MoveToFiltersEvent,
            ButtonCallback.ORGANISERS: MoveToOrganisersEvent,
        }[callback.data](),
        callback.message.from_user.id,
        callback.message.chat.id,
        callback.message.message_id,
    )
    '''
    try:
        state_machine = create_bot_state_machine()
        user = user_repository.read_or_create(get_default_user(callback.from_user.id))
        state = str_to_class_object(user.state_id)
        state = state_machine.handle(
            state,
            {
                ButtonCallback.MAIN_MENU: MoveToMainMenuEvent(),
                ButtonCallback.SCHEDULE: MoveToScheduleEvent(),
                ButtonCallback.MARKET: MoveToMarketEvent(),
                ButtonCallback.HOW_TO: MoveToHowToEvent(),
                ButtonCallback.CALENDAR: MoveToCalendarEvent(),
                ButtonCallback.FILTERS: MoveToFiltersEvent(),
                ButtonCallback.ORGANISERS: MoveToOrganisersEvent(user),
            }[callback.data]
        )
        edit_message(
            state,
            callback.message.chat.id,
            callback.message.message_id,
        )
        user.state_id = type(state).__qualname__
        user_repository.update(user)
    except Exception as e:
        sent_message = bot.send_message(callback.message.chat.id, 'Функция на стадии разработки')
        message_id = sent_message.message_id
        time.sleep(3 )
        bot.delete_message(message_id=message_id, chat_id=callback.message.chat.id)
        print(e)
'''
@bot.message_handler(func=lambda message: True)
def start(message):
    try:
        state_machine = create_bot_state_machine()
        user = user_repository.read_or_create(get_default_user(message.from_user.id))
        state = str_to_class_object(user.state_id)
        state = state_machine.handle(
            state,
            MoveToChoosePlaceState(state.match)
        )
        edit_message(
            state,
            message.chat.id,
            message.message_id,
        )
    except Exception as e:
        print(e)
'''

bot.polling(none_stop=True)
