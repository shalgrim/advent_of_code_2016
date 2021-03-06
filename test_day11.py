from unittest import TestCase

from day11_1 import Puzzle, shortest_path_solver


class TestDay11(TestCase):
    def setUp(self):
        self.floors = [
            ['HM', 'LM'],
            ['HG'],
            ['LG'],
            [],
        ]

    def test_part_1(self):
        p = Puzzle(self.floors)
        self.assertFalse(p.is_complete())
        self.assertTrue(p.is_valid())
        p.solve()
        self.assertEqual(p.seen_states[p.terminating_condition], 11)

    def test_bfs(self):
        self.assertEqual(shortest_path_solver(self.floors), 11)
