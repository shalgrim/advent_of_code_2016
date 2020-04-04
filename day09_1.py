from copy import copy


def decompress(s):
    remaining = copy(s)
    decompressed = ''

    while remaining:
        open_paren = remaining.find('(')
        if open_paren < 0:
            decompressed += remaining
            remaining = ''
        else:
            decompressed += remaining[:open_paren]
            remaining = remaining[open_paren:]
            close_paren = remaining.find(')')
            inside_parens = remaining[1:close_paren]
            chars_to_repeat, repeat_times = (
                int(inside_parens.split('x')[0]),
                int(inside_parens.split('x')[1]),
            )

            for _ in range(repeat_times):
                decompressed += remaining[
                    close_paren + 1 : close_paren + 1 + chars_to_repeat
                ]

            remaining = remaining[close_paren + 1 + chars_to_repeat :]

    return decompressed


if __name__ == '__main__':
    with open('./data/input09.txt') as f:
        txt = f.read()

    ins = ''.join(txt.split())  # remove whitespace
    print(len(decompress(ins)))

