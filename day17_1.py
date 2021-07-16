from hashlib import md5

GOAL = 3, 3
PUZZLE_INPUT = 'awrkjxxr'


def get_md5(code):
    ba = bytearray(code, 'utf-8')
    m = md5()
    m.update(ba)
    return m.hexdigest()


def get_door_status(code):
    return get_md5(code)[:4]


def get_next_steps(position, code):
    next_steps = []
    door_statuses = get_door_status(code)
    if door_statuses[0] in 'bcdef' and position[1] != 0:
        next_steps.append('U')

    if door_statuses[1] in 'bcdef' and position[1] != 3:
        next_steps.append('D')

    if door_statuses[2] in 'bcdef' and position[0] != 0:
        next_steps.append('L')

    if door_statuses[3] in 'bcdef' and position[0] != 3:
        next_steps.append('R')

    return next_steps


def get_next_position(position, step):
    if step == 'U':
        return position[0], position[1] - 1
    if step == 'D':
        return position[0], position[1] + 1
    if step == 'L':
        return position[0] - 1, position[1]
    if step == 'R':
        return position[0] + 1, position[1]


def find_shortest_path(passcode):
    """Because this grid is small and the goal is shortest, do BFS"""
    x, y = 0, 0
    states = [((x, y), passcode)]

    while not any([state[0] == GOAL for state in states]):
        new_states = []

        # extend search
        for position, code in states:
            next_steps = get_next_steps(position, code)
            for step in next_steps:
                new_position = get_next_position(position, step)
                new_states.append((new_position, code + step))

        states = new_states

    for state in states:
        if state[0] == GOAL:
            return state[1].removeprefix(passcode)


if __name__ == '__main__':
    print(find_shortest_path(PUZZLE_INPUT))
