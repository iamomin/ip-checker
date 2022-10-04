import unittest
from utils.api import IfConfig


class TestingApiEndPointIntegration(unittest.TestCase):

    def test_fetch_what_is_my_ip(self):
        i = IfConfig()
        response = i.what_is_my_ip()

        self.assertTrue(response is not None, "Response should not be none")
        self.assertTrue('ip' in response, "Response should contain ip address")
        self.assertTrue('country' in response, "Response should contain country")
        self.assertTrue('latitude' in response, "Response should contain latitude")
        self.assertTrue('longitude' in response, "Response should contain longitude")


if __name__ == '__main__':
    unittest.main()
