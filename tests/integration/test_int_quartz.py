import unittest
from datetime import datetime, timedelta

import constants as c
from utils.quartz import Scheduler
from utils.common import TimeParser


class TestingQuartzSchedulerIntegration(unittest.TestCase):

    def _get_sample(self) -> None:
        samples = 3
        dups = 2
        interval = 2

        samples = [
            datetime.strftime(datetime.today() + timedelta(seconds=(interval + (x if x >= dups else 1))), c.TIME_FORMAT)
            for x in range(samples)
        ]

        return TimeParser().parse(','.join(samples))

    def test_job_scheduler_without_time_slots(self):

        scd = Scheduler()
        scd.run('', None)

        self.assertEqual(len(scd.s.queue), 0, "It should not schedule any job")

    def test_job_scheduler_with_time_slot_and_no_job(self):

        scd = Scheduler()
        scd.run(self._get_sample(), None)

        self.assertEqual(len(scd.s.queue), 0, "It should not schedule any job")

    def test_job_scheduler_with_time_slot_and_with_job(self):
        scd = Scheduler()
        scd.run(self._get_sample(), lambda: True)

        self.assertEqual(len(scd.events), 3, "It should schedule 3 jobs")


if __name__ == '__main__':
    unittest.main()
