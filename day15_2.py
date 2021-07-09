#!/usr/bin/python
from day15_1 import Disc, does_capsule_pass, parse_discs


def main(raw_input_lines):
    t = 0
    discs = parse_discs(raw_input_lines)
    discs.append(Disc(11, 0))
    while not does_capsule_pass(discs, t):
        t += 1
    return t


if __name__ == '__main__':
    with open('data/input15.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))
