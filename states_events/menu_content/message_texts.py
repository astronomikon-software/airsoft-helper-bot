from model.match import Match
from repository.repository_initiation import *
from mapping.datetime_mapping import int_time_to_str
from mapping.loneliness_mapping import loneliness_to_str
from utils.text_util import escape_for_markdown as esc


class MessageText:
    HELLO = '''Здравия, товарищ!🤙

Данный бот предназначен для помощи страйкболисту, в поиске и организации игр.

Выбирай нужную опцию, чтобы узнать больше!

И подписывайся на автора данного проекта, Песец: @pesec_team
'''
    CHOOSE_FUNCTION = 'Выберите функцию:'
    SCHEDULE = '''Найди интересующую тебя игру!

✅ Поиск по датам. 
Просматривай календарь и не упусти не одной игры!

    ✅Поиск по фильтрам.
Ищешь конкретную игру от интересующих тебя организаторов? Или может быть ты ищешь ролевую игру или игру подходящую для новичков?
Теперь тебе не нужно перебирать тонны игр, используй фильтры и находи только интересные проекты!
'''
    HELP = 'По всем вопросам пишите @bait_media!'
    DONATE = '''Можете поддержать нас по ссылке:

https://www.donationalerts.com/r/danceegss

Там же оставить пожелания по доработке бота'''
    MARKET = 'Барахолка и форум находятся в разработке. Следите за новостями!'
    HOW_TO = 'О том, как начать играть, вы можете узнать по ссылке:' + '\n' + '\n' + 'https://vk.com/@spbstraik-kak-nachat-igrat-v-straikbol'
    ORGANISER_APPLICATION = 'Чтобы получить статус организатора, пришлите свой дикпик сюда:' + '\n' + '@bait_media'
    SET_NAME = 'Введите название игры:'
    SET_DATETIME = 'Введите дату и время в формате "ДД.ММ.ГГГГ ЧЧ:ММ":'
    CHOOSE_GENRE = '''Выберите тип мероприятия:
    
(Последовательно выберите нужное количество типов мероприятия, затем нажмите на кнопку "Перейти к следующему шагу")'''
    CHOOSE_GROUP = '''Выберите организаторов:
    
(Последовательно выберите нужное количество организаторов, затем нажмите на кнопку "Перейти к следующему шагу")'''
    CHOOSE_PLACE = 'Выберите место проведения:'
    CHOOSE_DURATION = 'Введите продолжительность игры:'
    CALENDAR = 'Календарь на стадии разработки'
    FILTERS = 'Выберите фильтр:'
    SET_PLACE = 'Введите полигон и адрес проведения:'
    SET_GROUP = '''Выберите организаторов:
    
(Последовательно выберите нужное количество организаторов, затем нажмите на кнопку "Перейти к следующему шагу")'''
    SET_GENRE = '''Выберите тип мероприятия:
    
(Последовательно выберите нужное количество типов мероприятия, затем нажмите на кнопку "Перейти к следующему шагу")'''
    SET_LONELINESS = 'Подходит ли игра для одиночек?'
    SET_URL = 'Отправьте ссылку на игру:'
    SET_ANNOTATION = 'Введите краткое описание игры:'
    SET_DURATION = 'Введите продолжительность игры:'
    CONFIRM_DATA = 'Подтвердите правильность введения данных'
    NEW_GAME_CREATED = 'Новая игра успешно создана!'
    NEW_GAME_CANCELLED = 'Отмена создания новой игры'
    SET_DATETIME_AGAIN = 'Формат данных неверен или введена некорректная дата. Попробуйте снова.' + '\n' + '\n' + \
                         'Введите дату и время в формате "ДД.ММ.ГГГГ ЧЧ:ММ":'
    LIST_OF_MATCHES = 'Выберите матч, чтобы увидеть полную информацию:'
    CHOOSE_LONELINESS_STATUS = 'Выберите, должна ли игра подходить одиночкам:'
    CHOOSE_DATE = 'Выберите дату, чтобы проверить наличие игр:'
    GAME_UPDATED = 'Данные об игре успешно изменены!'
    CURRENT_MATCH = 'Старая версия игры:'
    UPDATING_MATCH = 'Текущее состояние игры:'
    UPDATING_PROCESS = 'Выберите параметр для изменения или сохраните игру:'
    INSURE_UPDATING = 'Вы уверены, что хотите внести изменения в игру?'
    GAME_UPDATING_IS_CANCELLED = 'Редактирование игры отменено.'
    NO_MATCHES_FOUND = 'Не найдено игр в данной категории'
    NO_MATCHES_FOUND_THIS_DAY = 'Не найдено игр на выбранную дату'
    SUBSCRIPTION = 'Вы можете оформить подписку, чтобы получать уведовления о появлении новых игр в расписании!'
    SUBSCRIPTION_CREATED = 'Подписка успешно оформлена!'
    SUBSCRIPTION_ALREADY_EXISTS = 'Вы уже подписаны на уведомления о новых играх'
    SUBSCRIPTION_DELETED = 'Подписка отменена'
    SUBSCRIPTION_DOESNT_EXIST = 'Вы ещё не подписаны на уведомления о новых играх'

    @staticmethod
    def match_data(match: Match) -> str:
        groups = ''
        for i in range(len(match.group_id)):
            groups += group_repository.read_by_id(match.group_id[i]).name
            if i < len(match.group_id) - 1:
                groups += ', '

        genres = ''
        for i in range(len(match.genre_id)):
            genres += genre_repository.read_by_id(match.genre_id[i]).name
            if i < len(match.genre_id) - 1:
                genres += ', '

        return '\n'.join([
            f'- <b>Название:</b> {esc(match.name)}',
            f'- <b>Дата начала:</b> {esc(int_time_to_str(match.start_time))}',
            f'- <b>Продолжительность:</b> {esc(match.duration)}',
            f'- <b>Место проведения:</b> {esc(match.place_name)}',
            f'- <b>Организаторы:</b> {esc(groups)}\n',
            f'- <b>Тип мероприятия:</b> {esc(genres)}\n',
            f'- <b>Подходит ли для одиночек:</b> {esc(loneliness_to_str(match.is_loneliness_friendly))}',
            f'- <b>Ссылка на игру:</b> {esc(match.url)}',
            f'- <b>Краткое описание:</b> {esc(match.annotation)}'
        ])

    @staticmethod
    def new_match_announcement(match: Match) -> str:
        return 'Добавлена новая игра' + '\n' + '\n' + MessageText.match_data(match)

    @staticmethod
    def delayed_announcement(matches: list[Match]) -> str:
        matches_text = ''
        for match in matches:
            matches_text += '\n' + '\n' + MessageText.match_data(match)
        return 'Уже через пять дней состоится игра!' + matches_text
