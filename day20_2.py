def split_line(line):
    s1, s2 = line.split("-")
    return int(s1), int(s2)


def get_ranges(lines):
    ranges = [split_line(line) for line in lines]
    range_dict = {r[0]: r[1] for r in ranges}
    return range_dict


def find_a_lowest(range_dict, start):
    verified = False
    answer = start + 1
    while not verified:
        while answer in range_dict:
            answer = range_dict[answer] + 1
        for k, v in range_dict.items():
            if k <= answer <= v:
                answer = v + 1
                break
        else:
            verified = True
    return answer


def main(lines):
    range_dict = get_ranges(lines)
    highest_possible = 4_294_967_295
    known_blocked = -1
    answer = 0
    while True:  # TODO: terminating condition has something to do with highest_possible
        lowest = find_a_lowest(range_dict, known_blocked)
        if lowest > highest_possible:
            break
        # NEXT: Now that I've found a lowest unblocked
        # Find the next lowest blocked one, which should be easy
        # Then do some subtraction
        # and set known_blocked to the hi of that range
        # and loop
    return answer


if __name__ == "__main__":  # 356,899 is too low
    with open("data/input20.txt") as f:
        lines = [line.strip() for line in f]
    print(main(lines))
