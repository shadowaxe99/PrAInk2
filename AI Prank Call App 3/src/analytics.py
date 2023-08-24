class Analytics:
    def __init__(self):
        self.data = {}

    def track_call(self, phone_number, duration, pricing_plan):
        if phone_number not in self.data:
            self.data[phone_number] = []
        self.data[phone_number].append({'duration': duration, 'pricing_plan': pricing_plan})

    def get_data(self, phone_number):
        return self.data.get(phone_number, [])