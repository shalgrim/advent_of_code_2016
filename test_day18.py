from day18_1 import get_next_row


def test_get_next_row():
    example1 = ['..^^.', '.^^^^', '^^..^']
    for i in range(len(example1) - 1):
        assert get_next_row(example1[i]) == example1[i + 1]

    example2 = [
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
    for i in range(len(example2) - 1):
        assert get_next_row(example2[i]) == example2[i + 1]

