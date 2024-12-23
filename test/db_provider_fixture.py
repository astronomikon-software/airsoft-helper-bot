import pytest
from data.db_provider import DbProvider
from configuration import PSQL_PASSWORD


@pytest.fixture()  
def db_fixture():
    db_provider = DbProvider(
        database='cross_shooting',
        user='postgres',
        password=PSQL_PASSWORD,
        autocommit=False
    )
    db_provider.begin()
    yield db_provider
    db_provider.rollback()
