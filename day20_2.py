from day20_1 import get_ranges, find_a_lowest


def main(lines):
    range_dict = get_ranges(lines)
    highest_possible = 4_294_967_295  # max possible IP address?
    known_blocked = -1
    answer = 0
    while known_blocked < highest_possible:
        lowest = find_a_lowest(range_dict, known_blocked)
        if lowest > highest_possible:
            break
        answer = lowest
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
