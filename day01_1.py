def manhattan_distance(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])


def process_move(facing, turn, steps, from_pos):
    if turn == 'R':
        if facing == 'N':
            new_dir = 'E'
        elif facing == 'E':
            new_dir = 'S'
        elif facing == 'S':
            new_dir = 'W'
        elif facing == 'W':
            new_dir = 'N'
        else:
            raise Exception('wut 2')
    elif turn == 'L':
        if facing == 'N':
            new_dir = 'W'
        elif facing == 'W':
            new_dir = 'S'
        elif facing == 'S':
            new_dir = 'E'
        elif facing == 'E':
            new_dir = 'N'
        else:
            raise Exception('wut 2')
    else:
        raise Exception('wut 3')

    if new_dir == 'N':
        new_pos = from_pos[0], from_pos[1] - steps
    elif new_dir == 'E':
        new_pos = from_pos[0] + steps, from_pos[1]
    elif new_dir == 'S':
        new_pos = from_pos[0], from_pos[1] + steps
    elif new_dir == 'W':
        new_pos = from_pos[0] - steps, from_pos[1]
    else:
        raise Exception('wut 4')

    return new_dir, new_pos


def walk(instructions, start_pos=(0, 0)):
    pos = start_pos
    facing = 'N'

    for instruction in instructions:
        direction = instruction[0]
        steps = int(instruction[1:])
        facing, pos = process_move(facing, direction, steps, pos)

    return pos


def main(content):
    instructions = [c.strip() for c in content.split(',')]
    pos = walk(instructions)
    return manhattan_distance((0, 0), pos)


if __name__ == '__main__':
    with open('data/input01.txt') as f:
        content = f.read()
    print(main(content))  # 927 is too high
