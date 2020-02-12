from unittest import TestCase

from day04_1 import is_real_room


class TestDay04(TestCase):
    def test_is_real_room(self):
        self.assertTrue(is_real_room('aaaaa-bbb-z-y-x-123[abxyz]'))
        self.assertTrue(is_real_room('a-b-c-d-e-f-g-h-987[abcde]'))
        self.assertTrue(is_real_room('not-a-real-room-404[oarel]'))
        self.assertFalse(is_real_room('totally-real-room-200[decoy]'))
