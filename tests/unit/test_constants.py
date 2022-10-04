import unittest
import constants as c


class TestingConstants(unittest.TestCase):

    def test_config_file(self):
        self.assertEqual(c.CONF_FILE, 'config.ini', 'It should be expected config file name')

    def test_time_format(self):
        self.assertEqual(c.TIME_FORMAT, '%H:%M:%S', 'It should be expected time format')

    def test_api_url(self):
        self.assertEqual(c.API_URL, 'https://ifconfig.co/json', 'It should be valid api end point url')


if __name__ == '__main__':
    unittest.main()
