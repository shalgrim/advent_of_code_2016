def rotate(c, num):
    if c == '-':
        return ' '

    outc = c
    for _ in range(num):
        if outc == 'z':
            outc = 'a'
        else:
            outc = chr(ord(outc)+1)

    return outc


def decrypt(name, sector_id):
    outchars = []
    for c in name:
        outchars.append(rotate(c, sector_id))

    return ''.join(outchars)


def parse_name_and_sector_id(line):
    ending = line.split('-')[-1]
    sector_id = int(ending.split('[')[0])
    rindex = line.rfind('-')
    name = line[:rindex]
    return name, sector_id


def decrypt_all_lines(lines):
    to_decrypt = [parse_name_and_sector_id(line) for line in lines]
    decrypted = [decrypt(name, sector_id) for name, sector_id in to_decrypt]
    return decrypted


if __name__ == '__main__':
    with open('data/input04.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    decrypted_lines = decrypt_all_lines(lines)
    for i, dl in enumerate(decrypted_lines):
        if 'north' in dl:
            np_index = i
            break
    print('\n'.join(decrypted_lines))
    print('\n', lines[np_index])
