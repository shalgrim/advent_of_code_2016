from unittest import TestCase
from day02_1 import get_code
from day02_2 import get_button_star, hexify


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

    def test_part_2(self):
        self.assertEqual(get_code(self.instructions, get_button_star, hexify), '5DB3')
