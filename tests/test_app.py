import unittest

from app import add

class LogicaTestCase(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)