from unittest import TestCase

from day07_1 import has_abba, has_abba_in_brackets, supports_tls


class TestDay07(TestCase):
    def testHasAbba(self):
        self.assertTrue(has_abba('abba[mnop]qrst'))
        self.assertTrue(has_abba('abcd[bddb]xyyx'))
        self.assertFalse(has_abba('aaaa[qwer]tyui'))
        self.assertTrue(
            has_abba(
                'luqpeubugunvgzdqk[jfnihalscclrffkxqz]wvzpvmpfiehevybbgpg[esjuempbtmfmwwmqa]rhflhjrqjbbsadjnyc'
            )
        )

    def testHasAbbaInBrackets(self):
        self.assertTrue(has_abba_in_brackets('abcd[bddb]xyyx'))
        self.assertFalse(has_abba_in_brackets('aaaa[qwer]tyui'))
        self.assertTrue(
            has_abba_in_brackets(
                'luqpeubugunvgzdqk[jfnihalscclrffkxqz]wvzpvmpfiehevybbgpg[esjuempbtmfmwwmqa]rhflhjrqjbbsadjnyc'
            )
        )

    def testSupportsTls(self):
        self.assertTrue(supports_tls('abba[mnop]qrst'))
        self.assertFalse(supports_tls('abcd[bddb]xyyx'))
        self.assertFalse(supports_tls('aaaa[qwer]tyui'))
        self.assertTrue(supports_tls('ioxxoj[asdfgh]zxcvbn'))
        self.assertFalse(
            supports_tls(
                'luqpeubugunvgzdqk[jfnihalscclrffkxqz]wvzpvmpfiehevybbgpg[esjuempbtmfmwwmqa]rhflhjrqjbbsadjnyc'
            )
        )
