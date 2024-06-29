import pytest
from repository.genre_repository import GenreRepository
from db_provider_fixture import db_fixture


@pytest.fixture()
def genre_repository_fixture(db_fixture):
    repository = GenreRepository(db_fixture)
    return repository
