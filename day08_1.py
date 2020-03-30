def mapper(c):
    if c == 1:
        return '#'
    return '.'


def print_grid(grid):
    lines = []
    for row in grid:
        line = ''.join([mapper(c) for c in row])
        lines.append(line)
    print('\n'.join(lines))


def run_instruction(instruction, grid):
    # print('\nbefore\n', grid)
    if instruction.split()[0] == 'rect':
        width, height = instruction.split()[1].split('x')
        width, height = int(width), int(height)

        for y in range(height):
            for x in range(width):
                grid[y][x] = 1

    else:
        if instruction.split()[2][0] == 'y':
            y = int(instruction.split()[2].split('=')[1])
            amount = int(instruction.split()[-1])
            grid[y] = grid[y][-amount:] + grid[y][:-amount]
        else:
            grid_height = len(grid)
            x = int(instruction.split()[2].split('=')[1])
            amount = int(instruction.split()[-1])
            made_row = [grid[y][x] for y in range(grid_height)]
            made_row = made_row[-amount:] + made_row[:-amount]
            for y in range(grid_height):
                grid[y][x] = made_row[y]
    # print('\nafter\n', grid)


def run_program(instructions, grid_width=50, grid_height=6):
    grid = []
    for _ in range(grid_height):
        grid.append([0] * grid_width)
    for instruction in instructions:
        run_instruction(instruction, grid)

    return grid


def num_pixels_lit(grid):
    return sum(sum(row) for row in grid)


if __name__ == '__main__':
    with open('data/input08.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    grid = run_program(lines)
    print(num_pixels_lit(grid))
    print_grid(grid)
