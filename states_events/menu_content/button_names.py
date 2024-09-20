from model.match import Match
from repository.repository_initiation import place_repository
from mapping.datetime_mapping import int_time_to_str


class ButtonName:
    MAIN_MENU = 'Главное меню'
    SCHEDULE = 'Расписание игр'
    HOW_TO = 'Как начать играть в страйкбол'
    MARKET = 'Барахолка'
    CALENDAR = 'Просмотр календаря'
    FILTERS = 'Просмотр по фильтрам'
    ORGANISERS = 'Организаторам'
    GO_BACK = 'Назад' # ◀️
    GENRES = 'Просмотр по жанрам'
    GROUPS = 'Просмотр по орг.группам'
    PLACES = 'Просмотр по полигонам'
    LONELINESS = 'Подходит ли для одиночек'
    NEW_GAME = 'Внесение новой игры'
    UPDATE_GAME = 'Редактирование существующей игры'
    SET_ADMIN = 'Назначить организатора'
    YES = 'Да'
    NO = 'Нет'
    SAVE_GAME = 'Сохранить игру'
    CANCEL_GAME_EDITING = 'Отмена'
    BACK_TO_ORGANISERS = 'Меню организатора'
    START_UPDATING = 'Начать редактирование'
    NEXT_PAGE = '>'
    PREVIOUS_PAGE = '<'
    UPDATE_START_TIME = 'Изменить дату и время начала'
    UPDATE_PLACE = 'Изменить полигон'
    UPDATE_GROUP = 'Изменить огр.группу'
    UPDATE_GENRE = 'Изменить жанр'
    UPDATE_LONELINESS = 'Изменить одиноковость'


    def small_match_data(match: Match) -> str:
        return int_time_to_str(match.start_time) + ', ' + place_repository.read_by_id(match.place_id).name
