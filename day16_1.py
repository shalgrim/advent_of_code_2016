PUZZLE_INPUT = '11101000110010100'


def generate(a):
    b = ''.join(['0' if c == '1' else '1' for c in a[::-1]])
    return f'{a}0{b}'
