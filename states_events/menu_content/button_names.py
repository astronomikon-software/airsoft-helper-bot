from model.match import Match
from repository.repository_initiation import place_repository
from mapping.datetime_mapping import int_time_to_str


class ButtonName:
    MAIN_MENU = 'Главное меню'
    SCHEDULE = '🗓️ Расписание игр 🗓️'
    HOW_TO = '🔫 Как начать играть в страйкбол 🔫'
    MARKET = '💰 Барахолка 💰' 
    HELP = '🛑 Помощь 🛑'
    DONATE = '💸 Поддержать проект 💸'
    CALENDAR = '📋 Все игры 📋'
    FILTERS = '🎯 Просмотр по фильтрам 🎯'
    ORGANISERS = '🛠️ Организаторам 🛠️'
    GO_BACK = 'Назад' # ◀️
    GENRES = '📝 Просмотр по жанрам 📝'
    DATES = '🗓️ Просмотр календаря 🗓️'
    GROUPS = '👾 Просмотр по организаторам 👾'
    PLACES = '🚩 Просмотр по местам проведения 🚩'
    DURATION = '🕐 Просмотр по продолжительности 🕐'
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
    NEXT_STEP = 'Перейти к следующему шагу'
    UPDATE_NAME = 'Изменить название'
    UPDATE_START_TIME = 'Изменить дату начала'
    UPDATE_DURATION = 'Изменить продолжительность'
    UPDATE_PLACE = 'Изменить место проведения'
    UPDATE_GROUP = 'Изменить огранизаторов'
    UPDATE_GENRE = 'Изменить тип мероприятия'
    UPDATE_LONELINESS = 'Изменить одиноковость'
    UPDATE_URL = 'Изменить ссылку'
    UPDATE_ANNOTATION = 'Изменить краткое описание'
    SUBSCRIBE = '✍🏻 Оформить подписку ✍🏻'
    CREATE_SUBSCRIPTION = 'Подписаться на уведомления'
    DELETE_SUBSCRIPTION = 'Отказаться от подписки'


    def small_match_data(match: Match) -> str:
        return match.name + ', ' + int_time_to_str(match.start_time)
