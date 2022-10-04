import unittest
import run


class TestingRun(unittest.TestCase):

    def test_generate_test_sample(self):
        samples = run.generate_test_sample()
        self.assertEqual(len(samples.split(',')), 5, "It should be 5 samples")


if __name__ == '__main__':
    unittest.main()
