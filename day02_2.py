from day02_1 import get_code


def get_button_star(move, button):
    if move == 'U':
        if button in [3, 13]:
            return button - 2
        elif 6 <= button <= 12 and button != 9:
            return button - 4
        else:
            return button
    elif move == 'R':
        if button in [1, 4, 9, 12, 13]:
            return button
        else:
            return button + 1
    elif move == 'L':
        if button in [1, 2, 5, 10, 13]:
            return button
        else:
            return button - 1
    elif move == 'D':
        if button in [1, 11]:
            return button + 2
        elif 2 <= button <= 8 and button != 5:
            return button + 4
        else:
            return button


def hexify(numbers):
    return ''.join([hex(n)[-1].upper() for n in numbers])


if __name__ == '__main__':
    with open('data/input02.txt') as f:
        instructions = [line.strip() for line in f.readlines()]
    print(get_code(instructions, get_button_star, hexify))  # 2772A is wrong
