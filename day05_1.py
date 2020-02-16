from hashlib import md5


INPUT = 'reyedfim'


def get_hex_digest(room, index):
    s = room + str(index)
    ba = bytearray(s, 'utf-8')
    m = md5()
    m.update(ba)
    return m.hexdigest()


def get_door_password(door_id):
    outstr = ''
    index = 0

    while len(outstr) < 8:
        while get_hex_digest(door_id, index)[:5] != '00000':
            index += 1
        outstr += get_hex_digest(door_id, index)[5]
        index += 1

    return outstr


if __name__ == '__main__':
    print(get_door_password(INPUT))  # 'ce75ded3' is incorrect...'f97c354d' is correct
