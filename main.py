import telebot
from telebot import types
from configuration import BOT_TOKEN, PSQL_DATABASE, PSQL_USER, PSQL_PASSWORD

from data.db_provider import DbProvider
from repository.user_repository import UserRepository

from states_events.events import MainMenuEvent
from states_events.event_handler import handle_event
from states_events.states import StartState
from states_events.state_handler import handle_state

from utils.user_util import get_default_user
from utils.event_difiner import define_button_event, define_message_event


#maybe relocation of all repository initiations to separate module isn't a bad idea
db_provider = DbProvider(
    database=PSQL_DATABASE,
    user=PSQL_USER,
    password=PSQL_PASSWORD
)
user_repository = UserRepository(db_provider)

user_states = {}

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def toll_the_great_bell_once(message):
    try:
        user = user_repository.read_or_create(get_default_user(message.from_user.id))
        global user_states
        user_states[user.id] = StartState()
        state = handle_event(user_states[user.id], MainMenuEvent())
        screen_content = handle_state(state)
        bot.send_message(message.chat.id, screen_content.message_text, reply_markup=screen_content.markup)
        #handle_state(state)
        #user.state_id = state_to_json_str(state)
        #user_repository.update(user)
        user_states[user.id] = state
        # ^ temporary mera
    except Exception as E:
        print(E)


@bot.callback_query_handler(func=lambda callback: True)
def toll_the_great_bell_twice(callback):
    try:
        user = user_repository.read_or_create(get_default_user(callback.message.from_user.id))
        global user_states
        old_state = user_states[user.id]
        event = define_button_event(callback.data)
        state = handle_event(old_state, event)
        screen_content = handle_state(state)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, text=screen_content.message_text)
        bot.edit_message_reply_markup(chat_id=callback.message.chat.id, message_id=callback.message.message_id, reply_markup=screen_content.markup)
        user_states[user.id] = state
    except Exception as E:
        print(E)

bot.infinity_polling()
