from model.user import User


class UserRepository:

    async def create(self, user_id: int) -> User:
        pass
    
    async def read_by_id(self, user_id: int):
        pass

    async def change_state_id(self, state_id: int):
        pass
    
    async def set_admin(self, user: User):
        pass

    async def dismiss_admin(self, user: User):
        pass
    
    async def is_admin_check(self, is_admin: bool, is_true_admin: bool):
        pass

    