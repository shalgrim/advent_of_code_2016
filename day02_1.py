def get_button(move, button):
    if move == 'U':
        return button - 3 if button > 3 else button
    elif move == 'R':
        return button + 1 if button % 3 else button
    elif move == 'L':
        return button - 1 if button % 3 != 1 else button
    elif move == 'D':
        return button + 3 if button < 7 else button


def get_code(instructions):
    code_digits = []
    button = 5

    for instruction in instructions:
        for move in instruction:
            button = get_button(move, button)
        code_digits.append(button)

    return int(''.join([str(d) for d in code_digits]))


if __name__ == '__main__':
    with open('data/input02.txt') as f:
        instructions = [line.strip() for line in f.readlines()]
    print(get_code(instructions))
