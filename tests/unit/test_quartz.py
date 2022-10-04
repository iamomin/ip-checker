import unittest
from utils.quartz import Scheduler


class TestingQuartz(unittest.TestCase):

    def setUp(self):
        self.scheduler = Scheduler()

    def test_calculate_interval(self):
        self.scheduler.raw_times = {
            '12:13:37': 2,
            '12:13:38': 1
        }

        intervals = self.scheduler._calculate_interval()

        self.assertEqual(len(intervals), 2, "It should calculate 2 intervals objects")


if __name__ == '__main__':
    unittest.main()
