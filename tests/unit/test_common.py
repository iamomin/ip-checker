import unittest
from utils.common import TimeParser, Logger


class TestingTimeParser(unittest.TestCase):

    def setUp(self):
        self.tp = TimeParser()

    def test_logger_init(self):
        self.assertTrue(self.tp.logger is not None, "It should contain logger object")

    def test_parse(self):
        arg = '06:28:10,11:05:35,11:05:35'
        u_times = self.tp.parse(arg)

        self.assertTrue(u_times is not None, "It should return not None response")
        self.assertEqual(u_times['11:05:35'], 2, "It should detect key with duplicate count")
        self.assertEqual(u_times['06:28:10'], 1, "It should detect key with single count")
        self.assertEqual(len(u_times.keys()), 2, "It should detect two times")


if __name__ == '__main__':
    unittest.main()
