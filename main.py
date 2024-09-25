import telebot

from configuration import BOT_TOKEN

from repository.repository_initiation import *

from states_events.events import BotEvent, ButtonEvent, MessageEvent
from states_events.event_handler import get_new_state
from states_events.states import StartState
from states_events.presentation import ScreenPresentation, get_presentation

from utils.user_util import get_default_user


bot = telebot.TeleBot(BOT_TOKEN)


def handle_event(event: BotEvent, user_id: int) -> ScreenPresentation:
    user = user_repository.read_or_create(get_default_user(user_id=user_id))
    state = state_repository.read_or_create(state=StartState(), user_id=user.id)
    state = get_new_state(state=state, event=event, user=user)
    screen_presentation = get_presentation(state=state, user=user)
    state_repository.update(state=state, user_id=user.id)
    return screen_presentation

@bot.message_handler()
def toll_the_great_bell_once(message):
    try:
        screen_presentation = handle_event(
            event=MessageEvent(text=message.text),
            user_id=message.chat.id
        )
        bot.send_message(
            chat_id=message.chat.id, 
            text=screen_presentation.message_text, 
            reply_markup=screen_presentation.markup
        )
    except Exception as E:
        print(E)


@bot.callback_query_handler(func=lambda callback: True)
def toll_the_great_bell_thrice(callback):
    try:
        screen_presentation = handle_event(
            event=ButtonEvent(callback=callback.data),
            user_id=callback.message.chat.id
        )
        bot.edit_message_text(
            chat_id=callback.message.chat.id, 
            message_id=callback.message.message_id, 
            text=screen_presentation.message_text
        )
        bot.edit_message_reply_markup(
            chat_id=callback.message.chat.id, 
            message_id=callback.message.message_id, 
            reply_markup=screen_presentation.markup
        )
    except Exception as E:
        print(E)

bot.infinity_polling()

# Я посвящаю эту работу своим великим учителям: Артемию и Анне.
