import unittest
from requests import get_A1, get_A2, get_A3

class TestRequests(unittest.TestCase):

    def test_A1(self):
        result = get_A1()
        self.assertIsInstance(result, list)
        self.assertTrue(result, "нужен не пустой список")
        self.assertIsInstance(result[0], tuple)
        self.assertEqual(len(result[0]), 3)

    def test_A2(self):
        result = get_A2()
        self.assertIsInstance(result, list)
        self.assertTrue(result, "нужен не пустой список")
        salaries = [item[1] for item in result]
        self.assertEqual(salaries, sorted(salaries, reverse=True))
        if len(salaries) > 1:
            self.assertGreaterEqual(salaries[0], salaries[-1])

    def test_A3(self):
        result = get_A3()
        self.assertIsInstance(result, dict)
        for key in result:
            self.assertIn('оркестр', key)
            self.assertIsInstance(result[key], list)