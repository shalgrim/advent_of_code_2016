from unittest import TestCase
from day09_1 import decompress
from day09_2 import decompress_v2, len_decompress_v2


class TestDecompress(TestCase):
    def test_decompress(self):
        self.assertEqual('ADVENT', decompress('ADVENT'))
        self.assertEqual('ABBBBBC', decompress('A(1x5)BC'))
        self.assertEqual('ABCBCDEFEFG', decompress('A(2x2)BCD(2x2)EFG'))
        self.assertEqual('(1x3)A', decompress('(6x1)(1x3)A'))
        self.assertEqual('X(3x3)ABC(3x3)ABCY', decompress('X(8x2)(3x3)ABCY'))


class TestDecompressV2(TestCase):
    def test_decompress_v2(self):
        self.assertEqual('XYZXYZXYZ', decompress_v2('(3x3)XYZ'))
        self.assertEqual('XABCABCABCABCABCABCY', decompress_v2('X(8x2)(3x3)ABCY'))
        self.assertEqual('A' * 241920, decompress_v2('(27x12)(20x12)(13x14)(7x10)(1x12)A'))
        self.assertEqual(445, len(decompress_v2('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN')))


class TestLenDecompressV2(TestCase):
    def test_len_decompress_v2(self):
        self.assertEqual(len('XYZXYZXYZ'), len_decompress_v2('(3x3)XYZ'))
        self.assertEqual(len('XABCABCABCABCABCABCY'), len_decompress_v2('X(8x2)(3x3)ABCY'))
        self.assertEqual(241920, len_decompress_v2('(27x12)(20x12)(13x14)(7x10)(1x12)A'))
        self.assertEqual(445, len_decompress_v2('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'))
