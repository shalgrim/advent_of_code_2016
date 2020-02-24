from unittest import TestCase
from day07_1 import supports_tls, has_abba_in_brackets, has_abba


class TestDay07(TestCase):
    def testHasAbba(self):
        self.assertTrue(has_abba('abba[mnop]qrst'))
        self.assertTrue(has_abba('abcd[bddb]xyyx'))

    def testHasAbbaInBrackets(self):
        self.assertTrue(has_abba_in_brackets('abcd[bddb]xyyx'))

    def testSupportsTls(self):
        self.assertTrue(supports_tls('abba[mnop]qrst'))
        self.assertFalse(supports_tls('abcd[bddb]xyyx'))
