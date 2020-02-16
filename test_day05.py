from unittest import TestCase
from day05_1 import get_door_password


class TestDay05(TestCase):
    def test_get_door_password(self):
        self.assertEqual(get_door_password('abc'), '18f47a30')
