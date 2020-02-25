from unittest import TestCase
from day07_1 import supports_tls, has_abba_in_brackets, has_abba


class TestDay07(TestCase):
    def testHasAbba(self):
        self.assertTrue(has_abba('abba[mnop]qrst'))
        self.assertTrue(has_abba('abcd[bddb]xyyx'))
        self.assertFalse(has_abba('aaaa[qwer]tyui'))

    def testHasAbbaInBrackets(self):
        self.assertTrue(has_abba_in_brackets('abcd[bddb]xyyx'))
        self.assertFalse(has_abba_in_brackets('aaaa[qwer]tyui'))

    def testSupportsTls(self):
        self.assertTrue(supports_tls('abba[mnop]qrst'))
        self.assertFalse(supports_tls('abcd[bddb]xyyx'))
        self.assertFalse(supports_tls('aaaa[qwer]tyui'))
        self.assertTrue(supports_tls('ioxxoj[asdfgh]zxcvbn'))
