from copy import copy

from day09_1 import decompress


def decompress_v2(s):
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

            string_to_repeat = remaining[close_paren+1 : close_paren + 1 + chars_to_repeat]
            repeated_string = decompress_v2(string_to_repeat)

            for _ in range(repeat_times):
                decompressed += repeated_string

            remaining = remaining[close_paren + 1 + chars_to_repeat :]

    return decompressed


def len_decompress_v2(s):
    remaining = copy(s)
    answer = 0

    while remaining:
        open_paren = remaining.find('(')
        if open_paren < 0:
            answer += len(remaining)
            remaining = ''
        else:
            answer += open_paren
            remaining = remaining[open_paren:]
            close_paren = remaining.find(')')
            inside_parens = remaining[1:close_paren]
            chars_to_repeat, repeat_times = (
                int(inside_parens.split('x')[0]),
                int(inside_parens.split('x')[1]),
            )

            string_to_repeat = remaining[close_paren+1 : close_paren + 1 + chars_to_repeat]
            len_string_to_repeat = len_decompress_v2(string_to_repeat)
            answer += len_string_to_repeat * repeat_times
            remaining = remaining[close_paren + 1 + chars_to_repeat :]

    return answer


if __name__ == '__main__':
    with open('./data/input09.txt') as f:
        txt = f.read()

    ins = ''.join(txt.split())  # remove whitespace
    print(len_decompress_v2(ins))

