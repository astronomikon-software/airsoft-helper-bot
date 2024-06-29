from repository.match_repository import MatchRepository
from model.match import Match
from model.genre import Genre
from model.group import Group
from model.place import Place

from match_repository_fixture import match_repository_fixture


class TestMatchRepository:
    
    def test_create_and_read_all(self, match_repository_fixture):
        primary_matches = match_repository_fixture.read_all()
        
        match = Match()
        match.id = None
        match.start_time = 20240506200000
        match.duration = 20240506210000
        match.place_id = 1
        match.group_id = 2
        match.genre_id = 3
        match.is_loneliness_friendly = False

        match_repository_fixture.create(match)
        renewed_matches = match_repository_fixture.read_all()

        assert len(primary_matches) + 1 == len(renewed_matches)
        assert renewed_matches[-1].start_time == match.start_time
        assert renewed_matches[-1].duration == match.duration
        assert renewed_matches[-1].place_id == match.place_id
        assert renewed_matches[-1].group_id == match.group_id
        assert renewed_matches[-1].genre_id == match.genre_id
        assert renewed_matches[-1].is_loneliness_friendly == match.is_loneliness_friendly

    def test_update(self, match_repository_fixture):
        match = Match()
        match.id = 1
        match.start_time = 20240506200000
        match.duration = 20240506210000
        match.place_id = 2
        match.group_id = 2
        match.genre_id = 4
        match.is_loneliness_friendly = False

        match_repository_fixture.update(match)
        matches = match_repository_fixture.read_all()

        assert matches[-1].id == match.id
        assert matches[-1].place_id == match.place_id
        assert matches[-1].group_id == match.group_id
        assert matches[-1].duration == match.duration
        assert matches[-1].start_time == match.start_time
        assert matches[-1].genre_id == match.genre_id
        assert matches[-1].is_loneliness_friendly == match.is_loneliness_friendly

    def test_read_by_genre(self, match_repository_fixture):
        first_genre = Genre()
        first_genre.id = 1
        second_genre = Genre()
        second_genre.id = 2
        third_genre = Genre()
        third_genre.id = 3

        first_genre_matches = match_repository_fixture.read_by_genre(first_genre)
        second_genre_matches = match_repository_fixture.read_by_genre(second_genre)
        third_genre_matches = match_repository_fixture.read_by_genre(third_genre)

        assert len(first_genre_matches) == 1
        assert len(second_genre_matches) == 1
        assert len(third_genre_matches) == 1

        assert first_genre_matches[0].genre_id == 1
        assert second_genre_matches[0].genre_id == 2
        assert third_genre_matches[0].genre_id == 3

        assert first_genre_matches[0].id == 1
        assert second_genre_matches[0].id == 2
        assert third_genre_matches[0].id == 3

    def test_read_by_group(self, match_repository_fixture):
        first_group = Group()
        first_group.id = 1
        second_group = Group()
        second_group.id = 2
        third_group = Group()
        third_group.id = 3

        repository = match_repository_fixture
        first_group_matches = repository.read_by_group(first_group)
        second_group_matches = repository.read_by_group(second_group)
        third_group_matches = repository.read_by_group(third_group)

        assert len(first_group_matches) == 1
        assert len(second_group_matches) == 1
        assert len(third_group_matches) == 1

        assert first_group_matches[0].group_id == 1
        assert second_group_matches[0].group_id == 2
        assert third_group_matches[0].group_id == 3

        assert first_group_matches[0].id == 1
        assert second_group_matches[0].id == 2
        assert third_group_matches[0].id == 3

    def test_read_by_place(self, match_repository_fixture):
        first_place = Place()
        first_place.id = 1
        second_place = Place()
        second_place.id = 2
        third_place = Place()
        third_place.id = 3

        repository = match_repository_fixture
        first_place_matches = repository.read_by_place(first_place)
        second_place_matches = repository.read_by_place(second_place)
        third_place_matches = repository.read_by_place(third_place)

        assert len(first_place_matches) == 1
        assert len(second_place_matches) == 1
        assert len(third_place_matches) == 1

        assert first_place_matches[0].place_id == 1
        assert second_place_matches[0].place_id == 2
        assert third_place_matches[0].place_id == 3

        assert first_place_matches[0].id == 1
        assert second_place_matches[0].id == 2
        assert third_place_matches[0].id == 3
