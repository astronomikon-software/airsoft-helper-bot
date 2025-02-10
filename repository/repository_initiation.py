import config

from data.db_provider import DbProvider
from repository.genre_repository import GenreRepository
from repository.group_repository import GroupRepository
from repository.match_repository import MatchRepository
from repository.place_repository import PlaceRepository
from repository.state_repository import StateRepository
from repository.user_repository import UserRepository
from repository.subscription_repository import SubscriptionRepository
from repository.duration_repository import DurationRepository


db_provider = DbProvider(
    database=config.DB_NAME,
    user=config.DB_USER,
    password=config.DB_PASSWORD,
    host=config.DB_HOST,
    port=config.DB_PORT,
)

user_repository = UserRepository(db_provider)
state_repository = StateRepository(db_provider)
match_repository = MatchRepository(db_provider)
group_repository = GroupRepository(db_provider)
genre_repository = GenreRepository(db_provider)
place_repository = PlaceRepository(db_provider)
subscription_repository = SubscriptionRepository(db_provider)
duration_repository = DurationRepository(db_provider)
