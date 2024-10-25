from model.subscription import Subscription
from data.db_provider import DbProvider
from mapping.subscription_mapping import subscription_from_row


class SubscriptionRepository:

    def __init__(self, db_provider: DbProvider):
        self.db_provider = db_provider

    def create(self, subscription: Subscription):
        self.db_provider.execute_query(
            '''INSERT INTO subscriptions (user_id) VALUES (%s)''',
            (subscription.user_id,)
        )

    def read_all(self) -> list[Subscription]:
        rows = self.db_provider.execute_read_query('''SELECT * from subscriptions''')
        return list(map(subscription_from_row, rows))

    def read_by_user_id(self, user_id):
        row = self.db_provider.execute_read_query(
            '''SELECT * from subscriptions WHERE user_id = %s''',
            (user_id,)
        )
        return subscription_from_row(row[0])

    def delete(self, subscription: Subscription):
        self.db_provider.execute_query(
            '''DELETE FROM subscriptions WHERE id = %s''',
            (subscription.id,)
        )
