from insurance_event import InsuranceEvent

class StatsService:
    events = []

    maxes = {}
    sums = {}
    events_count = {}

    def ingest(self, event: InsuranceEvent):
        self.events.append(event)
        # We don't care if the events are lost, we only care about stats

        # update the max
        if event.user_id not in self.maxes:
            self.maxes[event.user_id] = event.amount
        else:
            if event.amount > self.maxes[event.user_id]:
                self.maxes[event.user_id] = event.amount

        # update the sum
        if event.user_id not in self.sums:
            self.sums[event.user_id] = 0

        self.sums[event.user_id] += event.amount

        # append the amount to be able to calculate the average later on
        if event.user_id not in self.events_count:
            self.events_count[event.user_id] = 0

        self.events_count[event.user_id] += 1

    def getSum(self, user_id: int) -> int:
        if user_id not in self.sums:
            raise Exception('User ID does not exist')

        return self.sums[user_id];

    def getMax(self, user_id: int) -> int:
        if user_id not in self.maxes:
            raise Exception('User ID does not exist')

        return self.maxes[user_id];

    def getAverage(self, user_id: int) -> int:
        if user_id not in self.events_count:
            raise Exception('User ID does not exist')

        if 0 == self.events_count[user_id]:
            # This should go along with the check above, but we can never be too sure
            raise Exception('No events have been yet ingested for this user')

        return int(self.getSum(user_id) / self.events_count[user_id])
