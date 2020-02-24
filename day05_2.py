from day05_1 import INPUT, get_hex_digest


def get_door_password_v2(door_id):
    out_positions = [None] * 8
    index = 0

    while None in out_positions:
        while get_hex_digest(door_id, index)[:5] != '00000':
            index += 1

        digest = get_hex_digest(door_id, index)
        try:
            position = int(digest[5])
        except ValueError:
            index += 1
            continue
        else:
            if position > 7 or out_positions[position] is not None:
                index += 1
                continue

        print(f'putting {digest[6]} in position {digest[5]}')
        out_positions[int(digest[5])] = digest[6]
        index += 1

    return ''.join(out_positions)


if __name__ == '__main__':
    print(get_door_password_v2(INPUT))
