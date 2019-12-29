def get_button(move, button):
    if move == 'U':
        return button - 3 if button > 3 else button
    elif move == 'R':
        return button + 1 if button % 3 else button
    elif move == 'L':
        return button - 1 if button % 3 != 1 else button
    elif move == 'D':
        return button + 3 if button < 7 else button


def decimalify(digits):
    return int(''.join([str(d) for d in digits]))


def get_code(instructions, button_getter=get_button, stringifier=decimalify):
    code_digits = []
    button = 5

    for instruction in instructions:
        for move in instruction:
            button = button_getter(move, button)
        code_digits.append(button)

    return stringifier(code_digits)


if __name__ == '__main__':
    with open('data/input02.txt') as f:
        instructions = [line.strip() for line in f.readlines()]
    print(get_code(instructions))
