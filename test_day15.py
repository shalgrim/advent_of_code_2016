from day15_1 import main


def test_main():
    test_lines = [
        'Disc #1 has 5 positions; at time=0, it is at position 4.',
        'Disc #2 has 2 positions; at time=0, it is at position 1.',
    ]
    assert main(test_lines) == 5
