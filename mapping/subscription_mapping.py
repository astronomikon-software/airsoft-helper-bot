from model.subscription import Subscription


def subscription_from_row(row: tuple) -> Subscription:
    subscription = Subscription()
    subscription.id = row[0]
    subscription.user_id = row[1]
    return subscription
