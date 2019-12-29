from enum import Enum, auto

from day01_1 import manhattan_distance


class Direction(Enum):
    NORTH = auto()
    EAST = auto()
    SOUTH = auto()
    WEST = auto()


DIRECTIONS = list(Direction)


def get_direction(existing_direction, turn):
    existing_index = DIRECTIONS.index(existing_direction)
    if turn == 'R':
        new_index = (existing_index + 1) % 4
    elif turn == 'L':
        new_index = existing_index - 1

    return DIRECTIONS[new_index]


def move(current_position, direction):
    if direction == Direction.NORTH:
        return current_position[0], current_position[1] - 1
    if direction == Direction.SOUTH:
        return current_position[0], current_position[1] + 1
    if direction == Direction.EAST:
        return current_position[0] + 1, current_position[1]
    if direction == Direction.WEST:
        return current_position[0] - 1, current_position[1]


def find_first_repeated_position(instructions):
    current_position = (0, 0)
    visited_positions = set([current_position])
    direction = Direction.NORTH

    for instruction in instructions:
        turn = instruction[0]
        steps = int(instruction[1:])
        direction = get_direction(direction, turn)

        for _ in range(steps):
            current_position = move(current_position, direction)
            if current_position in visited_positions:
                return current_position
            visited_positions.add(current_position)


def main(content):
    instructions = [c.strip() for c in content.split(',')]
    first_repeated = find_first_repeated_position(instructions)
    return manhattan_distance(first_repeated, (0, 0))


if __name__ == '__main__':
    with open('data/input01.txt') as f:
        content = f.read()
    print(main(content))
