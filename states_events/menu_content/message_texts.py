from model.match import Match
from repository.repository_initiation import *
from utils.datetime_util import int_datetime_to_str
from mapping.loneliness_mapping import loneliness_to_str


class MessageText:
    HELLO = 'Привет, друг! Это бот для организации матчей по страйкболу. Выбери нужную опцию, чтобы узнать больше!'
    CHOOSE_FUNCTION = 'Выберите функцию:'
    MARKET = 'Барахолка и форум находятся в разработке. Следите за новостями!'
    HOW_TO = 'О том, как начать играть, вы можете узнать по ссылке:' + '\n' + '\n' + 'https://www.youtube.com/watch?v=-LhUOF3XxBA'
    ORGANISER_APPLICATION = 'Чтобы получить статус организатора, пришлите свой дикпик сюда:' + '\n' + '@balt_media'
    SET_DATETIME = 'Введите дату и время в формате "ДД-ММ-ГГГГ ЧЧ:ММ":'
    CHOOSE_GENRE = 'Выберите жанр:'
    CHOOSE_GROUP = 'Выберите орг.группу:'
    CHOOSE_PLACE = 'Выберите полигон:'
    CALENDAR = 'Календарь на стадии разработки'
    FILTERS = 'Выберите фильтр:'
    SET_PLACE = 'Выберите полигон:'
    SET_GROUP = 'Выберите организационную группу:'
    SET_GENRE = 'Выберите жанр игры:'
    SET_LONELINESS = 'Подходит ли игра для одиночек?'
    CONFIRM_DATA = 'Подтвердите правильность введения данных'
    NEW_GAME_CREATED = 'Новая игра успешно создана!'

    def match_data(match: Match) -> str:
        return 'Дата и время начала:' + int_datetime_to_str(match.start_time) + \
            '\n' + 'Полигон:' + place_repository.read_by_id(match.place_id) + \
            '\n' + 'Организационная группа:' + group_repository.read_by_id(match.group_id) + \
            '\n' + 'Жанр игры:' + genre_repository.read_by_id(match.genre_id) + \
            '\n' + 'Подходит ли для одиночек:' + loneliness_to_str(match.is_loneliness_friendly)
