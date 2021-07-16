from copy import copy

from day17_1 import GOAL, PUZZLE_INPUT, get_next_position, get_next_steps


def find_all_paths(passcode, position=(0, 0)):
    """DFS"""
    next_steps = get_next_steps(position, passcode)
    paths = []

    for next_step in get_next_steps(position, passcode):
        next_position = get_next_position(position, next_step)
        if next_position == GOAL:
            paths.append(passcode + next_step)
        else:
            paths.extend(find_all_paths(passcode + next_step, next_position))

    return paths


def find_longest_path_length(passcode):
    all_paths = find_all_paths(passcode, (0, 0))
    max_path_len = max([len(path) for path in all_paths]) - len(passcode)
    return max_path_len


if __name__ == '__main__':
    print(find_longest_path_length(PUZZLE_INPUT))
