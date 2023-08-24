import stripe


class Subscription:
    def __init__(self):
        self.users = {}
        stripe.api_key = 'actual_stripe_api_key'

    def subscribe(self, user, plan):
        self.users[user] = plan
        stripe.Charge.create(
            amount=1000,  # amount in cents
            currency='usd',
            source='tok_visa',  # obtained with Stripe.js
            description='Charge for '+user
        )

    def unsubscribe(self, user):
        if user in self.users:
            del self.users[user]
        stripe.Charge.create(
            amount=1000,  # amount in cents
            currency='usd',
            source='tok_visa',  # obtained with Stripe.js
            description='Charge for '+user
        )

    def get_subscription(self, user):
        return self.users.get(user, 'free')