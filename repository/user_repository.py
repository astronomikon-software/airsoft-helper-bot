from model.user import User
from data.db_provider import DbProvider
from mapping.user_mapping import user_from_row


class UserRepository:
    
    def __init__(self, db_provider: DbProvider):
        self.db_provider = db_provider


    def create(self, user: User):
        self.db_provider.execute_query(
            '''INSERT INTO users (id, is_admin, is_true_admin) VALUES (%s, %s, %s)''',
            (
                user.id,
                user.is_admin,
                user.is_true_admin,
            )
        )
   
    def read_by_id(self, id: int) -> User:
        rows = self.db_provider.execute_read_query(
            '''SELECT * FROM users WHERE id = %s''',
            (id,)
        )
        return user_from_row(rows[0])

    def read_all(self) -> list[User]:
        rows = self.db_provider.execute_read_query('''SELECT * from users''')
        return list(map(user_from_row, rows))

    def update(self, user: User):
        self.db_provider.execute_query(
            '''UPDATE users SET is_admin = %s WHERE id = %s''', 
            (
                user.is_admin,
                user.id,
            )
        )   

    def read_or_create(self, user: User) -> User:
        try:
            return self.read_by_id(user.id)
        except:
            self.create(user)
            return user
