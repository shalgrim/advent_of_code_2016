import re

ABBA_PATT = re.compile(r'(.)(.)\2\1')
BRACKETED_ABBA_PATT = re.compile(r'\[[^\]]*(.)(.)\2\1\.*?]')


def has_abba_in_brackets(s):
    return matches_with_differing_groups(s, BRACKETED_ABBA_PATT)


def has_abba(s):
    return matches_with_differing_groups(s, ABBA_PATT)


def matches_with_differing_groups(s, pattern):
    match_groups = pattern.findall(s)
    if match_groups:
        for mg in match_groups:
            if mg[0] != mg[1]:
                return True
    return False


def supports_tls(s):
    if not has_abba_in_brackets(s) and has_abba(s):
        return True
    return False

