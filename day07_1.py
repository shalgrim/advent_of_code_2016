import re

ABBA_PATT = re.compile(r'(.)(.)\2\1')
BRACKETED_ABBA_PATT = re.compile(r'\[[^\]]*(.)(.)\2\1.*?\]')


def has_abba_in_brackets(s, debug=False):
    if debug:
        print('has_abba_in_brackets')
    return matches_with_differing_groups(s, BRACKETED_ABBA_PATT, debug)


def has_abba(s, debug=False):
    if debug:
        print('has_abba')
    return matches_with_differing_groups(s, ABBA_PATT, debug)


def matches_with_differing_groups(s, pattern, debug=False):
    match_groups = pattern.findall(s)
    if debug:
        print(match_groups)

    if match_groups:
        for mg in match_groups:
            if mg[0] != mg[1]:
                return True
    return False


def supports_tls(s, debug=False):
    if not has_abba_in_brackets(s, debug) and has_abba(s, debug):
        return True
    return False


if __name__ == '__main__':
    with open('data/input07.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    supported = [supports_tls(line) for line in lines]
    print(sum(supports_tls(line) for line in lines))  # 183 is too high
