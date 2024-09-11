from configuration import *

from data.db_provider import DbProvider
from repository.genre_repository import GenreRepository
from repository.group_repository import GroupRepository
from repository.match_repository import MatchRepository
from repository.place_repository import PlaceRepository
from repository.state_repository import StateRepository
from repository.user_repository import UserRepository


db_provider = DbProvider(
    database=PSQL_DATABASE,
    user=PSQL_USER,
    password=PSQL_PASSWORD
)

user_repository = UserRepository(db_provider)
state_repository = StateRepository(db_provider)
match_repository = MatchRepository(db_provider)
group_repository = GroupRepository(db_provider)
genre_repository = GenreRepository(db_provider)
place_repository = PlaceRepository(db_provider)
