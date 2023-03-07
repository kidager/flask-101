class InsuranceEvent:
    def __init__(self, user_id, timestamp, amount):
        self.user_id = user_id # int $ # // the insured user
        self.timestamp = timestamp # int $ #
        self.amount = amount # int $ # // € cents. positive or negative
