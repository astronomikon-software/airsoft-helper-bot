import pytest
from repository.place_repository import PlaceRepository
from db_provider_fixture import db_fixture


@pytest.fixture()
def place_repository_fixture(db_fixture):
    repository = PlaceRepository(db_fixture)
    return repository
