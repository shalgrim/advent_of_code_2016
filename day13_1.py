def is_wall(x, y, fave_num=1362):
    num = x * x + 3 * x + 2 * x * y + y + y * y
    num += fave_num
    binary = bin(num)
    s = str(binary)
    num_ones = len([c for c in s if c == '1'])
    return num_ones % 2 == 1


def bfs(start, destination):
    paths = [start]
    distance = 0
    distances = {start: distance}

    while destination not in paths:
        distance += 1
        new_paths = []

        for x, y in paths:
            potentials = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
            for next_x, next_y in potentials:
                if next_x < 0 or next_y < 0:
                    continue
                if is_wall(next_x, next_y):
                    continue
                if (next_x, next_y) in distances:
                    continue
                new_paths.append((next_x, next_y))
                distances[(next_x, next_y)] = distance

        paths = new_paths

    return distance


if __name__ == '__main__':
    print(bfs((1, 1), (7, 4)))
    print(bfs((1, 1), (31, 39)))
