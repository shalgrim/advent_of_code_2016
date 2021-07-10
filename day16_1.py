PUZZLE_INPUT = '11101000110010100'
# DISK_SIZE = 272
DISK_SIZE = 35_651_584


def generate(a):
    b = ''.join(['0' if c == '1' else '1' for c in a[::-1]])
    return f'{a}0{b}'


def checksum(data):
    checksum = ''
    while len(checksum) % 2 == 0:
        checksum = ''
        for i in range(0, len(data), 2):
            checksum += '1' if data[i] == data[i + 1] else '0'
        data = checksum

    return checksum


def main(initial_state, disk_size):
    new_data = initial_state
    while len(new_data) < disk_size:
        new_data = generate(new_data)

    return checksum(new_data[:disk_size])


if __name__ == '__main__':
    print(main(PUZZLE_INPUT, DISK_SIZE))
