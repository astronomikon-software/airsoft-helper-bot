from data.db_provider import DbProvider

from model.genre import Genre
from model.group import Group
from model.place import Place

from genre_repository_fixture import genre_repository_fixture
from group_repository_fixture import group_repository_fixture
from place_repository_fixture import place_repository_fixture


class TestGenreRepository:

    def test_read_all(self, genre_repository_fixture):
        genres = genre_repository_fixture.read_all()
        assert len(genres) == 3

    def test_read_by_id(self, genre_repository_fixture):
        genre_needed = genre_repository_fixture.read_by_id(1)
        assert genre_needed.name == 'Battle-Royal'

        genre_needed = genre_repository_fixture.read_by_id(2)
        assert genre_needed.name == 'King of the Mount'

        genre_needed = genre_repository_fixture.read_by_id(3)
        assert genre_needed.name == 'All Against All'

class TestGroupRepository:

    def test_read_all(self, group_repository_fixture):
        groups = group_repository_fixture.read_all()
        assert len(groups) == 4

    def test_read_by_id(self, group_repository_fixture):
        group_needed = group_repository_fixture.read_by_id(1)
        assert group_needed.name == 'Death Wolves'

        group_needed = group_repository_fixture.read_by_id(2)
        assert group_needed.name == 'Punkihoy'

        group_needed = group_repository_fixture.read_by_id(3)
        assert group_needed.name == 'Shoota Boyz'

        group_needed = group_repository_fixture.read_by_id(4)
        assert group_needed.name == 'Suicide Squad'

class TestPlaceRepository:

    def test_read_all(self, place_repository_fixture):
        places = place_repository_fixture.read_all()
        assert len(places) == 4

    def test_read_by_id(self, place_repository_fixture):
        place_needed = place_repository_fixture.read_by_id(1)
        assert place_needed.name == 'Totskiy Polygon'

        place_needed = place_repository_fixture.read_by_id(2)
        assert place_needed.name == 'Opushka'

        place_needed = place_repository_fixture.read_by_id(3)
        assert place_needed.name == 'Kolpino'

        place_needed = place_repository_fixture.read_by_id(4)
        assert place_needed.name == 'Sanctum Peterium Hive'
