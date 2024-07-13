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

@bot.message_handler(commands=['start'])
def start(message):
    try:
        user = User()
        user.id = message.from_user.id
        user.state_id = 1
        user.is_admin = False
        user.is_true_admin = False
        user_repository.create(user)
    except Exception as e:
        print(e)
        #db_provider.rollback()
    markup = types.InlineKeyboardMarkup()
    markup.add(create_button(ButtonName.SCHEDULE, ButtonCallback.SCHEDULE))
    markup.add(create_button(ButtonName.HOW_TO, ButtonCallback.HOW_TO))
    markup.add(create_button(ButtonName.MARKET, ButtonCallback.MARKET))
    bot.send_message(message.chat.id, text=MessageText.HELLO, reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_operator(callback):
    try:
        if callback.message:
            if callback.data == ButtonCallback.TO_MAIN_MENU:
                markup = types.InlineKeyboardMarkup()
                markup.add(create_button(ButtonName.SCHEDULE, ButtonCallback.SCHEDULE))
                markup.add(create_button(ButtonName.HOW_TO, ButtonCallback.HOW_TO))
                markup.add(create_button(ButtonName.MARKET, ButtonCallback.MARKET))
                bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, text=MessageText.HELLO)
                bot.edit_message_reply_markup(chat_id=callback.message.chat.id, message_id=callback.message.message_id, reply_markup=markup)
            
            elif callback.data == ButtonCallback.SCHEDULE:
                markup = types.InlineKeyboardMarkup()
                markup.add(create_button(ButtonName.CALENDAR, ButtonCallback.CALENDAR))
                markup.add(create_button(ButtonName.FILTERS, ButtonCallback.FILTERS))
                markup.add(create_button(ButtonName.ORGANISERS, ButtonCallback.ORGANISERS))
                markup.add(create_button(ButtonName.GO_BACK, ButtonCallback.TO_MAIN_MENU))
                bot.edit_message_text(chat_id=callback.message.chat.id,message_id=callback.message.message_id, text=MessageText.CHOOSE_FUNCTION)
                bot.edit_message_reply_markup(chat_id=callback.message.chat.id, message_id=callback.message.message_id, reply_markup=markup)
            
            elif callback.data == ButtonCallback.HOW_TO:
                markup = types.InlineKeyboardMarkup()
                markup.add(create_button(ButtonName.TO_MAIN_MENU, ButtonCallback.TO_MAIN_MENU))
                bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, text=MessageText.HOW_TO)
                bot.edit_message_reply_markup(chat_id=callback.message.chat.id, message_id=callback.message.message_id, reply_markup=markup)
            
            elif callback.data == ButtonCallback.MARKET:
                markup = types.InlineKeyboardMarkup()
                markup.add(create_button(ButtonName.TO_MAIN_MENU, ButtonCallback.TO_MAIN_MENU))
                bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, text=MessageText.MARKET)
                bot.edit_message_reply_markup(chat_id=callback.message.chat.id, message_id=callback.message.message_id, reply_markup=markup)
            
            elif callback.data == ButtonCallback.ORGANISERS:
                user = user_repository.read_by_id(callback.from_user.id)
                if user.is_admin == True:
                    markup = types.InlineKeyboardMarkup()
                    markup.add(create_button(ButtonName.NEW_GAME, ButtonCallback.NEW_GAME))
                    markup.add(create_button(ButtonName.UPDATE_GAME, ButtonCallback.UPDATE_GAME))
                    if user.is_true_admin == True:
                        markup.add(create_button(ButtonName.SET_ADMIN, ButtonCallback.SET_ADMIN))
                    markup.add(create_button(ButtonName.GO_BACK, ButtonCallback.SCHEDULE), create_button(ButtonName.TO_MAIN_MENU, ButtonCallback.TO_MAIN_MENU))
                    bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, text=MessageText.CHOOSE_FUNCTION)
                    bot.edit_message_reply_markup(chat_id=callback.message.chat.id, message_id=callback.message.message_id, reply_markup=markup)
                else:
                    markup = types.InlineKeyboardMarkup()
                    markup.add(create_button(ButtonName.TO_MAIN_MENU, ButtonCallback.TO_MAIN_MENU))
                    bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, text=MessageText.ORGANISER_APPLICATION)
                    bot.edit_message_reply_markup(chat_id=callback.message.chat.id, message_id=callback.message.message_id, reply_markup=markup)
            
            elif callback.data == ButtonCallback.NEW_GAME: #Убейте меня...
                markup = types.InlineKeyboardMarkup()
                match = Match()
                genres = genre_repository.read_all()
                groups = group_repository.read_all()
                places = place_repository.read_all()
                bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, text=MessageText.PRINT_DATETIME)
                bot.edit_message_reply_markup(chat_id=callback.message.chat.id, message_id=callback.message.message_id, reply_markup=markup)
                
                @bot.message_handler(regexp='\d{4}-\d{2}-\d{2} \d{2}:\d{2}')
                def start_time_handler(message):
                    match.start_time = str_to_int(message.text)
                    markup = types.InlineKeyboardMarkup()
                    for genre in genres:
                        button = create_button(f'{genre.name}', ButtonCallback.CHOOSE_GENRE + f'{genre.id}')
                        button.data = genre
                        markup.add(button)
                    bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.message_id, text=MessageText.CHOOSE_GENRE)
                    bot.edit_message_reply_markup(chat_id=callback.message.chat.id, message_id=callback.message.message_id, reply_markup=markup)

                @bot.callback_query_handler(func=lambda callback: True)
                def game_creator(callback):
                    try:
                        if callback.message:
                            if callback.data == ButtonCallback.CHOOSE_GENRE + f'{callback.data.id}':
                                match.genre_id = callback.data.id
                                # to do
                    except Exception as e:
                        print(e)
                                
            elif callback.data == ButtonCallback.UPDATE_GAME:
                pass
    
    except Exception as e:
        print(e)

bot.polling(none_stop=True)
