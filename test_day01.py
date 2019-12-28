from unittest import TestCase
from day01_1 import main


class TestDay01(TestCase):
    def test_day1_1(self):
        self.assertEqual(main('R2, L3'), 5)
        self.assertEqual(main('R2, R2, R2'), 2)
        self.assertEqual(main('R5, L5, R5, R3'), 12)
