from collections import Counter


def generate_checksum(name):
    counts = Counter(name)
    sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    checksum = ''.join([str(c) for c, _ in sorted_counts[:5]])
    return checksum


def is_real_room(line):
    name, checksum = line.split('[')
    checksum = checksum[:-1]
    name = name.split('-')
    name = ''.join(name[:-1])
    expected_checksum = generate_checksum(name)
    return expected_checksum == checksum


def get_sector_ids(lines):
    lines = [line.split('[')[0] for line in lines]
    sector_ids = [int(line.split('-')[-1]) for line in lines]
    return sector_ids


if __name__ == '__main__':
    with open('data/input04.txt') as f:
        lines = [line.strip() for line in f.readlines()]
    real = [is_real_room(line) for line in lines]
    sector_ids = get_sector_ids(lines)
    sum_real_rooms = 0
    for is_real, sector_id in zip(real, sector_ids):
        if is_real:
            sum_real_rooms += int(sector_id)
    print(sum_real_rooms)
