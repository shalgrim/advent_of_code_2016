def run_instruction(instruction, grid):
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
            grid[y] = grid[y][-amount:] + grid[y][amount:]
        else:
            x = int(instruction.split()[2].split('=')[1])
            amount = int(instruction.split()[-1])
            made_row = [grid[y][x] for y in range(6)]
            made_row = made_row[-amount:] + made_row[amount:]
            for y in range(6):
                grid[y][x] = made_row[y]


def run_program(instructions):
    grid = []
    for _ in range(6):
        grid.append([0] * 50)
    for instruction in instructions:
        run_instruction(instruction, grid)

    return grid


if __name__ == '__main__':
    with open('data/input08.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    grid = run_program(lines)