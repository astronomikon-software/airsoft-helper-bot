from model.match import Match
from repository.repository_initiation import place_repository
from mapping.datetime_mapping import int_time_to_str


class ButtonName:
    MAIN_MENU = 'Главное меню'
    SCHEDULE = '🗓️ Расписание игр 🗓️'
    HOW_TO = '🔫 Как начать играть в страйкбол 🔫'
    MARKET = '💰 Барахолка 💰' 
    HELP = '🛑 Помощь 🛑'
    CALENDAR = '🗓️ Просмотр календаря 🗓️'
    FILTERS = '🎯 Просмотр по фильтрам 🎯'
    ORGANISERS = '🛠️ Организаторам 🛠️'
    GO_BACK = 'Назад' # ◀️
    GENRES = '📝 Просмотр по жанрам 📝'
    GROUPS = '👾 Просмотр по орг.группам 👾'
    PLACES = '🚩 Просмотр по полигонам 🚩'
    LONELINESS = '✅ Подходит ли для одиночек ✅'
    NEW_GAME = 'Внесение новой игры'
    UPDATE_GAME = 'Редактирование существующей игры'
    SET_ADMIN = 'Назначить организатора'
    YES = '✅ Да ✅'
    NO = '❌ Нет ❌'
    SAVE_GAME = 'Сохранить игру'
    CANCEL_GAME_EDITING = 'Отмена'
    BACK_TO_ORGANISERS = 'Меню организатора'
    START_UPDATING = 'Начать редактирование'
    NEXT_PAGE = '>'
    PREVIOUS_PAGE = '<'
    UPDATE_NAME = 'Изменить имя'
    UPDATE_START_TIME = 'Изменить дату начала'
    UPDATE_PLACE = 'Изменить полигон'
    UPDATE_GROUP = 'Изменить огр.группу'
    UPDATE_GENRE = 'Изменить жанр'
    UPDATE_LONELINESS = 'Изменить одиноковость'
    UPDATE_URL = 'Изменить ссылку'
    SUBSCRIBE = 'Оформить подписку'
    CREATE_SUBSCRIPTION = 'Подписаться на уведомления'
    DELETE_SUBSCRIPTION = 'Отказаться от подписки'


    def small_match_data(match: Match) -> str:
        return match.name + ', ' + int_time_to_str(match.start_time)
