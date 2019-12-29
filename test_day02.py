from unittest import TestCase
from day02_1 import get_code


class TestDay02(TestCase):
    def setUp(self):
        self.instructions = [
            'ULL',
            'RRDDD',
            'LURDL',
            'UUUUD',
        ]

    def test_part_1(self):
        self.assertEqual(get_code(self.instructions), 1985)
