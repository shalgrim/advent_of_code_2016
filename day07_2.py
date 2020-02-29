import re

OUTSIDE_FIRST_PATT = re.compile(r'(.)(.)\1.*\[[^\]]*\2\1\2.*?\]')
INSIDE_FIRST_PATT = re.compile(r'\[[^\]]*(.)(.)\1.*?\].*\2\1\2.*')


def supports_ssl(s, debug=False):
    if OUTSIDE_FIRST_PATT.search(s) or INSIDE_FIRST_PATT.search(s):
        outside_first_groups = OUTSIDE_FIRST_PATT.findall(s)
        inside_first_groups = INSIDE_FIRST_PATT.findall(s)
        print(outside_first_groups)
        print(inside_first_groups)
        return True
    return False


if __name__ == '__main__':
    with open('data/input07.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    supported = [supports_ssl(line) for line in lines]
    print(sum(supported))  # 259 is too high
    # my guess is that the problem is that I don't ensure the _other_ occurence is _outside_
    # therefore my next step should be to develop test cases where I have the ABA and BAB both
    # occur inside and make that fail unless one is outside

    for i, line in enumerate(lines):
        if supports_ssl(line):
            print(i, line)
            supports_ssl(line, True)
