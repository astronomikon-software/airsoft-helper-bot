import pytest
from repository.user_repository import UserRepository
from db_provider_fixture import db_fixture


@pytest.fixture()
def user_repository_fixture(db_fixture):
    repository = UserRepository(db_fixture)
    return repository
