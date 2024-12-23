import pytest
from repository.match_repository import MatchRepository
from db_provider_fixture import db_fixture


@pytest.fixture()
def match_repository_fixture(db_fixture):
    repository = MatchRepository(db_fixture)
    return repository
