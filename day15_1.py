import re
from dataclasses import dataclass

PATTERN = re.compile(
    r'^Disc #\d has (\d+) positions?; at time=0, it is at position (\d+)\.$'
)


@dataclass
class Disc:
    positions: int
    initial_position: int

    def position_at_time(self, t):
        return (self.initial_position + t) % self.positions


def parse_discs(raw_input_lines):
    discs = [
        Disc(*[int(g) for g in PATTERN.match(line).groups()])
        for line in raw_input_lines
    ]
    return discs


def does_capsule_pass(discs, t):
    for disc in discs:
        t += 1
        if disc.position_at_time(t) != 0:
            return False
    return True


def main(raw_input_lines):
    t = 0
    discs = parse_discs(raw_input_lines)
    while not does_capsule_pass(discs, t):
        t += 1
    return t


if __name__ == '__main__':
    with open('data/input15.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    print(main(lines))
