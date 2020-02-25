import re

ABBA_PATT = re.compile(r'(.)(.)\2\1')
BRACKETED_ABBA_PATT = re.compile(r'\[[^\]]*(.)(.)\2\1\]')


def has_abba_in_brackets(s):
    return BRACKETED_ABBA_PATT.search(s) is not None


def has_abba(s):
    return ABBA_PATT.search(s) is not None


def supports_tls(s):
    if not has_abba_in_brackets(s) and has_abba(s):
        return True
    return False
