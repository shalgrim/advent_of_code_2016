from unittest import TestCase

from day11_1 import Puzzle


class TestDay11(TestCase):
    def test_part_1(self):
        floors = [
            ['HM', 'LM'],
            ['HG'],
            ['LG'],
            [],
        ]
        p = Puzzle(floors)
        self.assertFalse(p.is_complete())
        self.assertTrue(p.is_valid())
        p.solve()
        self.assertEqual(p.seen_states[p.terminating_condition], 11)
