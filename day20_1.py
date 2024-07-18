def split_line(line):
    s1, s2 = line.split("-")
    return int(s1), int(s2)


def main(lines):
    ranges = [split_line(line) for line in lines]
    range_dict = {r[0]: r[1] for r in ranges}
    verified = False
    answer = 0
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


if __name__ == "__main__":  # 356,899 is too low
    with open("data/input20.txt") as f:
        lines = [line.strip() for line in f]
    print(main(lines))
