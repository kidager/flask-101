from insurance_event import InsuranceEvent
from stats_service import StatsService
import pytest


class TestStatsService:
    stats_service_instance = StatsService()

    def test_get_sum(self):
        for event in [
            InsuranceEvent(user_id=1, timestamp=0, amount=100_00),
            InsuranceEvent(user_id=1, timestamp=0, amount=100_00),
            InsuranceEvent(user_id=1, timestamp=0, amount=20_00),
            InsuranceEvent(user_id=2, timestamp=0, amount=50_00),
            InsuranceEvent(user_id=2, timestamp=0, amount=1_00),
        ]:
            self.stats_service_instance.ingest(event)

        assert 220_00 == self.stats_service_instance.getSum(1)
        assert 51_00 == self.stats_service_instance.getSum(2)
        with pytest.raises(Exception):
            self.stats_service_instance.getSum(3)

    def test_get_max(self):
        for event in [
            InsuranceEvent(user_id=1, timestamp=0, amount=100_00),
            InsuranceEvent(user_id=1, timestamp=0, amount=100_00),
            InsuranceEvent(user_id=1, timestamp=0, amount=20_00),
            InsuranceEvent(user_id=2, timestamp=0, amount=50_00),
            InsuranceEvent(user_id=2, timestamp=0, amount=1_00),
        ]:
            self.stats_service_instance.ingest(event)

        assert 100_00 == self.stats_service_instance.getMax(1)
        assert 50_00 == self.stats_service_instance.getMax(2)
        with pytest.raises(Exception):
            self.stats_service_instance.getMax(3)

    def test_get_average(self):
        for event in [
            InsuranceEvent(user_id=1, timestamp=0, amount=100_00),
            InsuranceEvent(user_id=1, timestamp=0, amount=100_00),
            InsuranceEvent(user_id=1, timestamp=0, amount=20_00),
            InsuranceEvent(user_id=2, timestamp=0, amount=50_00),
            InsuranceEvent(user_id=2, timestamp=0, amount=1_00),
        ]:
            self.stats_service_instance.ingest(event)

        assert 73_33 == self.stats_service_instance.getAverage(1)
        assert 25_50 == self.stats_service_instance.getAverage(2)
        with pytest.raises(Exception):
            self.stats_service_instance.getAverage(3)
