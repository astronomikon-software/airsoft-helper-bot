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
        old_match = Match()
        old_match.id = 1
        old_match.start_time = 20240506200000
        old_match.duration = 20240506210000
        old_match.place_id = 2
        old_match.group_id = 2
        old_match.genre_id = 4
        old_match.is_loneliness_friendly = False
        match_repository_fixture.create(old_match)

        new_match = Match()
        new_match.id = 1
        new_match.start_time = 20240506203000
        new_match.duration = 20240506210300
        new_match.place_id = 1
        new_match.group_id = 1
        new_match.genre_id = 2
        new_match.is_loneliness_friendly = True
        match_repository_fixture.update(new_match)

        matches = match_repository_fixture.read_all()

        assert matches[-1].id == new_match.id
        assert matches[-1].place_id == new_match.place_id
        assert matches[-1].group_id == new_match.group_id
        assert matches[-1].duration == new_match.duration
        assert matches[-1].start_time == new_match.start_time
        assert matches[-1].genre_id == new_match.genre_id
        assert matches[-1].is_loneliness_friendly == new_match.is_loneliness_friendly

    def test_read_by_genre(self, match_repository_fixture):
        first_match = Match()
        first_match.id = 1
        first_match.start_time = 20240506200000
        first_match.duration = 20240506210000
        first_match.place_id = 1
        first_match.group_id = 1
        first_match.genre_id = 1
        first_match.is_loneliness_friendly = False
        match_repository_fixture.create(first_match)

        second_match = Match()
        second_match.id = 2
        second_match.start_time = 20240506203000
        second_match.duration = 20240506210300
        second_match.place_id = 1
        second_match.group_id = 1
        second_match.genre_id = 1
        second_match.is_loneliness_friendly = True
        match_repository_fixture.create(second_match)

        third_match = Match()
        third_match.id = 3
        third_match.start_time = 20240506203000
        third_match.duration = 20240506210300
        third_match.place_id = 2
        third_match.group_id = 2
        third_match.genre_id = 2
        third_match.is_loneliness_friendly = True
        match_repository_fixture.create(third_match)

        genre = Genre()
        genre.id = 1
        matches = match_repository_fixture.read_by_genre(genre)

        assert len(matches) == 2
        assert matches[0].genre_id == 1
        assert matches[1].genre_id == 1
        assert matches[0].id == 1
        assert matches[1].id == 2

    def test_read_by_group(self, match_repository_fixture):
        first_match = Match()
        first_match.id = 1
        first_match.start_time = 20240506200000
        first_match.duration = 20240506210000
        first_match.place_id = 1
        first_match.group_id = 1
        first_match.genre_id = 1
        first_match.is_loneliness_friendly = False
        match_repository_fixture.create(first_match)

        second_match = Match()
        second_match.id = 2
        second_match.start_time = 20240506203000
        second_match.duration = 20240506210300
        second_match.place_id = 1
        second_match.group_id = 1
        second_match.genre_id = 1
        second_match.is_loneliness_friendly = True
        match_repository_fixture.create(second_match)

        third_match = Match()
        third_match.id = 3
        third_match.start_time = 20240506203000
        third_match.duration = 20240506210300
        third_match.place_id = 2
        third_match.group_id = 2
        third_match.genre_id = 2
        third_match.is_loneliness_friendly = True
        match_repository_fixture.create(third_match)

        group = Group()
        group.id = 1
        matches = match_repository_fixture.read_by_group(group)

        assert len(matches) == 2
        assert matches[0].group_id == 1
        assert matches[1].group_id == 1
        assert matches[0].id == 1
        assert matches[1].id == 2

    def test_read_by_place(self, match_repository_fixture):
        first_match = Match()
        first_match.id = 1
        first_match.start_time = 20240506200000
        first_match.duration = 20240506210000
        first_match.place_id = 1
        first_match.group_id = 1
        first_match.genre_id = 1
        first_match.is_loneliness_friendly = False
        match_repository_fixture.create(first_match)

        second_match = Match()
        second_match.id = 2
        second_match.start_time = 20240506203000
        second_match.duration = 20240506210300
        second_match.place_id = 1
        second_match.group_id = 1
        second_match.genre_id = 1
        second_match.is_loneliness_friendly = True
        match_repository_fixture.create(second_match)

        third_match = Match()
        third_match.id = 3
        third_match.start_time = 20240506203000
        third_match.duration = 20240506210300
        third_match.place_id = 2
        third_match.group_id = 2
        third_match.genre_id = 2
        third_match.is_loneliness_friendly = True
        match_repository_fixture.create(third_match)

        place = Place()
        place.id = 1
        matches = match_repository_fixture.read_by_genre(place)

        assert len(matches) == 2
        assert matches[0].place_id == 1
        assert matches[1].place_id == 1
        assert matches[0].id == 1
        assert matches[1].id == 2
