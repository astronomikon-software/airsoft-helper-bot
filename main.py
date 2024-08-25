import telebot
from telebot import types
from configuration import BOT_TOKEN, PSQL_DATABASE, PSQL_USER, PSQL_PASSWORD

from data.db_provider import DbProvider
from repository.user_repository import UserRepository

from states_events.events import MainMenuEvent
from states_events.event_handler import handle_event

from utils.user_util import get_default_user


#maybe relocation of all repository initiations to separate module isn't a bad idea
db_provider = DbProvider(
    database=PSQL_DATABASE,
    user=PSQL_USER,
    password=PSQL_PASSWORD
)
user_repository = UserRepository(db_provider)

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def toll_the_great_bell_once(message):
    try:
        user = user_repository.read_or_create(get_default_user(message.from_user.id))
        state = handle_event(user.state_id, MainMenuEvent)
        #state_content = get_state_content(state) -> will make buttons, callbacks, messages
        #user.state_id = state_to_json_str(state)
        #user_repository.update(user)
    except Exception as E:
        print(E)


@bot.callback_query_handler(func=lambda callback: True)
def toll_the_great_bell_twice(callback):
    pass
