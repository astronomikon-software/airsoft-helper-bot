import telebot
from telebot import types
from configuration import BOT_TOKEN

from menu_buttons.message_text import MessageText
from menu_buttons.create_button import create_button
from menu_buttons.button_name import ButtonName
from menu_buttons.button_callback import ButtonCallback




bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
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
    except Exception as e:
        print(e)

bot.polling(none_stop=True)
