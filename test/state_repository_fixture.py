import pytest
from db_provider_fixture import db_fixture
from repository.state_repository import StateRepository


@pytest.fixture()
def state_repository_fixture(db_fixture):
    repository = StateRepository(db_fixture)
    return repository