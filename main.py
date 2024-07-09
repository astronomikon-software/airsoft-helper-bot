import telebot
from telebot import types
from configuration import BOT_TOKEN
from menu_buttons.buttons import to_main_menu_button
from menu_buttons.buttons import MainMenuButtons, ScheduleButtons, FilterButtons
from menu_buttons.button_callback import ButtonCallback


bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    buttons = MainMenuButtons()
    markup.add(buttons.button1)
    markup.add(buttons.button2)
    markup.add(buttons.button3)
    bot.send_message(message.chat.id, 'Привет, друг! Это бот для организации матчей по страйкболу. Выбери нужную опцию, чтобы узнать больше!', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def schedule_layer(callback):
    try:
        if callback.data == ButtonCallback.TO_MAIN_MENU:
            markup = types.InlineKeyboardMarkup()
            buttons = MainMenuButtons()
            markup.add(buttons.button1)
            markup.add(buttons.button2)
            markup.add(buttons.button3)
            bot.send_message(callback.message.chat.id, 'Привет, друг! Это бот для организации матчей по страйкболу. Выбери нужную опцию, чтобы узнать больше!', reply_markup=markup)
        elif callback.data == ButtonCallback.SCHEDULE:
            markup = types.InlineKeyboardMarkup()
            buttons = ScheduleButtons()
            markup.add(buttons.button1)
            markup.add(buttons.button2)
            markup.add(buttons.button3)
            markup.add(buttons.go_back_button)
            bot.send_message(callback.message.chat.id, 'Выберите функцию:', reply_markup=markup)
        elif callback.data == ButtonCallback.MARKET:
            markup = types.InlineKeyboardMarkup()
            markup.add(to_main_menu_button)
            bot.send_message(callback.message.chat.id, 'Барахолка и форум находятся в разработке. Следите за новостями!', reply_markup=markup)
    except Exception as e:
        print(e)

bot.polling(none_stop=True)
