from unittest import TestCase
from day09_1 import decompress


class TestDecompress(TestCase):
    def test_decompress(self):
        self.assertEqual('ADVENT', decompress('ADVENT'))
        self.assertEqual('ABBBBBC', decompress('A(1x5)BC'))
        self.assertEqual('ABCBCDEFEFG', decompress('A(2x2)BCD(2x2)EFG'))
        self.assertEqual('(1x3)A', decompress('(6x1)(1x3)A'))
        self.assertEqual('X(3x3)ABC(3x3)ABCY', decompress('X(8x2)(3x3)ABCY'))
