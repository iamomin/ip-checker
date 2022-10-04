import unittest
from utils.common import TimeParser


class TestingTimeParserIntegration(unittest.TestCase):

    def setUp(self):
        self.tp = TimeParser()

    def test_time_string_parse(self):
        arg = ' 09:15:25 ,11:58:23,13:45:09, 09:15:25 '

        u_times = self.tp.parse(arg)

        self.assertTrue(u_times is not None, "It should return not None response")
        self.assertEqual(u_times['09:15:25'], 2, "It should detect key with duplicate count")
        self.assertEqual(u_times['11:58:23'], 1, "It should detect key with single count")
        self.assertEqual(len(u_times.keys()), 3, "It should detect three times")


if __name__ == '__main__':
    unittest.main()
