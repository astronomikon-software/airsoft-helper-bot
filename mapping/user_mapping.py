from model.user import User


def user_from_row(row: tuple) -> User:
    user = User()
    user.id = row[0]
    user.is_admin = row[1]
    user.is_true_admin = row[2]
    return user
