import re

OUTSIDE_FIRST_PATT = re.compile(r'(?:\]|^)[^\[]*(.)(.)\1.*\[[^\]]*\2\1\2.*?\]')
INSIDE_FIRST_PATT = re.compile(r'\[[^\]]*(.)(.)\1.*?\][^\[]*\2\1\2.*')


def supports_ssl(s, debug=False):
    if OUTSIDE_FIRST_PATT.search(s) or INSIDE_FIRST_PATT.search(s):
        outside_first_groups = OUTSIDE_FIRST_PATT.findall(s)
        inside_first_groups = INSIDE_FIRST_PATT.findall(s)
        return True
    return False


if __name__ == '__main__':
    with open('data/input07.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    supported = [supports_ssl(line) for line in lines]
    print(sum(supported))  # 259 is too high
