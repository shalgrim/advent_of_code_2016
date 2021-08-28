SAFE = '.'
TRAP = '^'
TRAP_INDICATORS = [
    (TRAP, TRAP, SAFE),
    (SAFE, TRAP, TRAP),
    (TRAP, SAFE, SAFE),
    (SAFE, SAFE, TRAP),
]
TRAP_STRINGS = [''.join(t) for t in TRAP_INDICATORS]


def get_next_row(row):
    next_row = [TRAP] if row[1] == TRAP else [SAFE]
    next_row += [TRAP if row[i - 1 : i + 2] in TRAP_STRINGS else SAFE for i in range(1, len(row) - 1)]
    next_row.append(TRAP if row[-2] == TRAP else SAFE)

    return ''.join(next_row)
