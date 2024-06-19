from model.user import User

from data.execution import execute_query
from data.read_all_execution import execute_read_query

from mapping.user_mapping import user_from_row



class UserRepository:

    def create(self, user: User):
        execute_query(
            '''INSERT INTO users (id, state_id, is_admin, is_true_admin) VALUES (%s, %s, %s, %s)''',
            (
                user.id,
                user.state_id,
                user.is_admin,
                user.is_true_admin,
            )
        )
   
    def read_by_id(self, user: User) -> User:
        row = execute_read_query(
            '''SELECT * FROM users WHERE id = %s''',
            (user.id,)
        )
        return user_from_row(row)

    def update(self, user: User):
        execute_query(
            '''UPDATE users SET state_id = %s, is_admin = %s WHERE id = %s''', 
            (
                user.state_id,
                user.is_admin,
                user.id,
            )
        )   
