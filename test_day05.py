from unittest import TestCase
from day05_1 import get_door_password
from day05_2 import get_door_password_v2


class TestDay05(TestCase):
    def test_get_door_password(self):
        self.assertEqual(get_door_password('abc'), '18f47a30')

    def test_part_two(self):
        self.assertEqual(get_door_password_v2('abc'), '05ace8e3')
