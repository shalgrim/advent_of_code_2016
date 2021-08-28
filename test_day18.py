from day18_1 import build_map, get_next_row, num_safe_tiles

EXAMPLE_1 = ['..^^.', '.^^^^', '^^..^']

EXAMPLE_2 = [
    '.^^.^.^^^^',
    '^^^...^..^',
    '^.^^.^.^^.',
    '..^^...^^^',
    '.^^^^.^^.^',
    '^^..^.^^..',
    '^^^^..^^^.',
    '^..^^^^.^^',
    '.^^^..^.^^',
    '^^.^^^..^^',
]


def test_get_next_row():
    example1 = ['..^^.', '.^^^^', '^^..^']
    for i in range(len(example1) - 1):
        assert get_next_row(example1[i]) == example1[i + 1]

    for i in range(len(EXAMPLE_2) - 1):
        assert get_next_row(EXAMPLE_2[i]) == EXAMPLE_2[i + 1]


def test_build_map():
    map = build_map(EXAMPLE_1[0], len(EXAMPLE_1))
    assert map == EXAMPLE_1
    map = build_map(EXAMPLE_2[0], len(EXAMPLE_2))
    assert map == EXAMPLE_2


