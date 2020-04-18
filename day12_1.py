
def run_program(lines):
    registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
    iptr = 0

    def intize(val):
        try:
            return int(val)
        except ValueError:
            return registers[val]

    def process_instruction(instruction):
        components = instruction.split()

        if components[0] == 'cpy':
            registers[components[2]] = intize(components[1])
            jumpby = 1
        elif components[0] == 'inc':
            registers[components[1]] += 1
            jumpby = 1
        elif components[0] == 'dec':
            registers[components[1]] -= 1
            jumpby = 1
        elif components[0] == 'jnz':
            x, y = [intize(c) for c in components[1:]]
            jumpby = y if x != 0 else 1

        return jumpby

    while iptr < len(lines):
        iptr += process_instruction(lines[iptr])

    return registers['a']


if __name__ == '__main__':
    with open('data/input12.txt') as f:
        lines = [line.strip() for line in f.readlines()]

    print(run_program(lines))
