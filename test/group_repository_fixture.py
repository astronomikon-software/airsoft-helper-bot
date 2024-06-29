import pytest
from repository.group_repository import GroupRepository
from db_provider_fixture import db_fixture


@pytest.fixture()
def group_repository_fixture(db_fixture):
    repository = GroupRepository(db_fixture)
    return repository
