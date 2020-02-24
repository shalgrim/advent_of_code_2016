from collections import Counter


if __name__ == '__main__':
    with open('data/input06.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    counters = []

    for i, _ in enumerate(range(len(lines[0]))):
        counter = Counter(line[i] for line in lines)
        counters.append(counter)

    most_common = [c.most_common()[-1][0] for c in counters]
    print(''.join(most_common))
