from day13_1 import is_wall


def dfs_count(max_steps, location=(1, 1), current_steps=0, visited=None):
    if visited is None:
        visited = {}

    if current_steps > max_steps:
        return

    visited[location] = current_steps
    x, y = location
    potentials = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    for potential in potentials:
        if potential in visited and visited[potential] <= current_steps + 1:
            continue
        if potential[0] < 0 or potential[1] < 0:
            continue
        if is_wall(*potential):
            continue
        dfs_count(max_steps, potential, current_steps+1, visited)

    return len(visited)


if __name__ == '__main__':
    print(dfs_count(50))
