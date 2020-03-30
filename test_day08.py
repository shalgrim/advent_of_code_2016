from unittest import TestCase

from day08_1 import run_program


class TestDay08(TestCase):
    def test_part_1(self):  # TODO: create a print_grid function to aid in debugging
        lines = [
            'rect 3x2',
            'rotate column x=1 by 1',
            'rotate row y=0 by 4',
            'rotate column x=1 by 1',
        ]
        grid = run_program(lines, 7, 3)
        self.assertEqual(
            grid, [[0, 1, 0, 0, 1, 0, 1], [1, 0, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0]]
        )
