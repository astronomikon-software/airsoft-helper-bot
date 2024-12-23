from model.user import User
from user_repository_fixture import user_repository_fixture
from configuration import PSQL_PASSWORD


class TestUserRepository:

    def test_create(self, user_repository_fixture):     
        user = User()
        user.id = 3
        user.state_id = 1
        user.is_admin = False
        user.is_true_admin = False

        user_repository_fixture.create(user)
        created_user = user_repository_fixture.read_by_id(user.id)

        assert created_user.id == user.id
        assert created_user.state_id == user.state_id
        assert created_user.is_admin == user.is_admin
        assert created_user.is_true_admin == user.is_true_admin

    def test_update(self, user_repository_fixture):
        user = User()
        user.id = 1
        user.state_id = 3
        user.is_admin = True
        user.is_true_admin = False

        user_repository_fixture.update(user)
        updated_user = user_repository_fixture.read_by_id(user.id)

        assert updated_user.id == user.id
        assert updated_user.state_id == user.state_id
        assert updated_user.is_admin == user.is_admin
        assert updated_user.is_true_admin == user.is_true_admin
