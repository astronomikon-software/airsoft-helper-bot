from model.match import Match
from repository.repository_initiation import *
from mapping.datetime_mapping import int_time_to_str
from mapping.loneliness_mapping import loneliness_to_str


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
    MARKET = 'Барахолка и форум находятся в разработке. Следите за новостями!'
    HOW_TO = 'О том, как начать играть, вы можете узнать по ссылке:' + '\n' + '\n' + 'https://vk.com/@spbstraik-kak-nachat-igrat-v-straikbol'
    ORGANISER_APPLICATION = 'Чтобы получить статус организатора, пришлите свой дикпик сюда:' + '\n' + '@bait_media'
    SET_NAME = 'Введите название игры:'
    SET_DATETIME = 'Введите дату в формате "ДД.ММ.ГГГГ":'
    CHOOSE_GENRE = 'Выберите тип мероприятия:'
    CHOOSE_GROUP = 'Выберите организатора:'
    CHOOSE_PLACE = 'Выберите место проведения:'
    CHOOSE_DURATION = 'Выберите вариант длительности игры:'
    CALENDAR = 'Календарь на стадии разработки'
    FILTERS = 'Выберите фильтр:'
    SET_PLACE = 'Введите название места проведения:'
    SET_GROUP = 'Выберите организатора:'
    SET_GENRE = 'Выберите тип мероприятия:'
    SET_LONELINESS = 'Подходит ли игра для одиночек?'
    SET_URL = 'Отправьте ссылку на игру:'
    SET_ANNOTATION = 'Введите краткое описание игры:'
    SET_DURATION = 'Выберите вариант длительности игры:'
    CONFIRM_DATA = 'Подтвердите правильность введения данных'
    NEW_GAME_CREATED = 'Новая игра успешно создана!'
    NEW_GAME_CANCELLED = 'Отмена создания новой игры'
    SET_DATETIME_AGAIN = 'Формат данных неверен или введена некорректная дата. Попробуйте снова.' + '\n' + '\n' + \
        'Введите дату и время в формате "ДД.ММ.ГГГГ":'
    LIST_OF_MATCHES = 'Выберите матч, чтобы увидеть полную информацию:'
    CHOOSE_LONELINESS_STATUS = 'Выберите, должна ли игра подходить одиночкам:'
    GAME_UPDATED = 'Данные об игре успешно изменены!'
    CURRENT_MATCH = 'Старая версия игры:'
    UPDATING_MATCH = 'Текущее состояние игры:'
    UPDATING_PROCESS = 'Выберите параметр для изменения или сохраните игру:'
    INSURE_UPDATING = 'Вы уверены, что хотите внести изменения в игру?'
    GAME_UPDATING_IS_CANCELLED = 'Редактирование игры отменено.'
    NO_MATCHES_FOUND = 'Не найдено игр в данной категории'
    SUBSCRIPTION = 'Вы можете оформить подписку, чтобы получать уведовления о появлении новых игр в расписании!'
    SUBSCRIPTION_CREATED = 'Подписка успешно оформлена!'
    SUBSCRIPTION_ALREADY_EXISTS = 'Вы уже подписаны на уведомления о новых играх'
    SUBSCRIPTION_DELETED = 'Подписка отменена'
    SUBSCRIPTION_DOESNT_EXIST = 'Вы ещё не подписаны на уведомления о новых играх'

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

        return 'Название:' + ' ' + match.name + \
            '\n' + 'Дата начала:' + ' ' + int_time_to_str(match.start_time) + \
            '\n' + 'Продолжительность:' + ' ' + match.place_name + \
            '\n' + 'Место проведения:' + ' ' + match.place_name + \
            '\n' + 'Организаторы:' + ' ' + groups + \
            '\n' + 'Тип мероприятия:' + ' ' + genres + \
            '\n' + 'Подходит ли для одиночек:' + ' ' + loneliness_to_str(match.is_loneliness_friendly) + \
            '\n' + 'Краткое описание:' + ' ' + loneliness_to_str(match.is_loneliness_friendly) + \
            '\n' + 'Ссылка на игру:' + ' ' + match.url + \
            '\n' + 'Краткое описание:' + ' ' + match.annotation
    
    def new_match_announcement(match: Match) -> str:
        return 'Добавлена новая игра' + '\n' + '\n' + MessageText.match_data(match)
    
    def delayed_announcement(matches: list[Match]) -> str:
        matches_text = ''
        for match in matches:
            matches_text += '\n' + '\n' + MessageText.match_data(match)
        return 'Уже через пять дней состоится игра!' + matches_text
